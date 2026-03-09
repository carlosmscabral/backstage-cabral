FROM node:20-slim

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install --only=production

COPY . .

# Run the web service on container startup.
CMD [ "npm", "start" ]
