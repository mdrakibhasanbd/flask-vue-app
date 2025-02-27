# Development Stage
FROM node:18.18.2-alpine AS development

WORKDIR /app

# Copy package.json and package-lock.json
COPY ./package*.json ./

# Install dependencies
RUN npm install

# Copy all source files
COPY . .

# Set the default command to start the development server
CMD ["npm", "run", "dev"]

# Production Stage
FROM node:18.18.2-alpine AS build

WORKDIR /app

# Copy package.json and package-lock.json
COPY ./package*.json ./

# Install all dependencies (production and development)
RUN npm install

# Copy all source files
COPY . .

# Build the production-ready files
RUN npm run build

# Serve Stage
FROM nginx:stable-alpine AS production

# Set the working directory in Nginx
WORKDIR /usr/share/nginx/html

# Copy built files from the build stage
COPY --from=build /app/dist ./

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Add custom Nginx configuration
COPY ./nginx/nginx.conf /etc/nginx/conf.d

# Expose the port on which Nginx will run
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
