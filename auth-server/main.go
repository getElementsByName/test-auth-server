package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"

	"github.com/golang-jwt/jwt"
)

func indexMiddleware(w http.ResponseWriter, req *http.Request) {
	fmt.Fprintf(w, "Auth Server\n")
}

func healthcheckMiddleware(w http.ResponseWriter, req *http.Request) {
	fmt.Fprintf(w, "OK")
}

const AUTH_HEADER_NAME = "Authorization"
const VALUE_TYPE = "Bearer"

func jwtAuthMiddleware(w http.ResponseWriter, req *http.Request) {
	var rawAuthHeaderValue = req.Header.Get(AUTH_HEADER_NAME)
	var jwtValue = strings.TrimLeft(strings.TrimLeft(rawAuthHeaderValue, VALUE_TYPE), " ")

	tokenString := jwtValue
	loggerDebug.Print(tokenString)

	// Parse takes the token string and a function for looking up the key. The latter is especially
	// useful if you use multiple keys for your application.  The standard is to use 'kid' in the
	// head of the token to identify which key to use, but the parsed token (head and claims) is provided
	// to the callback, providing flexibility.
	token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
		// Don't forget to validate the alg is what you expect:
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, fmt.Errorf("Unexpected signing method: %v", token.Header["alg"])
		}

		// hmacSampleSecret is a []byte containing your secret, e.g. []byte("my_secret_key")
		return hmacSecret, nil
	})

	if err != nil {
		w.WriteHeader(400)
		fmt.Println(err)
		fmt.Fprintf(w, fmt.Sprintf("%#v", err))
		return
	}

	if claims, ok := token.Claims.(jwt.MapClaims); ok && token.Valid {
		var sub = claims["sub"].(string)
		w.Header().Set("JWT-AUTH-SUB", sub)
		fmt.Fprintf(w, "OK")
		return
	} else {
		w.WriteHeader(400)
		fmt.Fprintf(w, "token unvalid")
		return
	}
}

var loggerInfo *log.Logger
var loggerDebug *log.Logger
var hmacSecret []byte

func main() {
	loggerInfo = log.New(os.Stdout, "INFO: ", log.LstdFlags)
	loggerDebug = log.New(os.Stdout, "DEBUG: ", log.LstdFlags)

	var Port = os.Getenv("PORT")
	hmacSecret = []byte(os.Getenv("HMAC_SECRET"))
	loggerDebug.Printf("SECRET: " + string(hmacSecret))

	http.HandleFunc("/", indexMiddleware)
	http.HandleFunc("/jwt-auth", jwtAuthMiddleware)
	http.HandleFunc("/healthcheck", healthcheckMiddleware)

	loggerInfo.Print(fmt.Sprintf("Start (port: %v)\n", Port))
	http.ListenAndServe(":"+Port, nil)
}
