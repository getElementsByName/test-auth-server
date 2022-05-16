ARG BASE_IMAGE_FULLNAME=

FROM golang:1.18 as builder

WORKDIR /workspace/app
COPY ./ /workspace/app/

RUN go build /workspace/app/main.go


FROM ${BASE_IMAGE_FULLNAME}
USER root

WORKDIR /workspace/app
COPY --from=builder /workspace/app /workspace/app

ENTRYPOINT ["/workspace/app/main"]