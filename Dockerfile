# syntax=docker/dockerfile:1
FROM node:16

WORKDIR /app
COPY . .
RUN yarn install && yarn vuepress:build