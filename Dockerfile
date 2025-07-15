FROM python:bookworm
WORKDIR /Users/rt/Documents/ai-agent
EXPOSE 8000
CMD [ "python3","-m","http.server","8000" ]

