# Build
To build the project navigate to a folder where `docker-compose.yml` is located and create `.env` file based on `.env.example` provided in the repository.

Make sure you have [**Docker**](https://docs.docker.com/engine/install/) installed.

Then run ` sudo docker compose up --build -d` to build the project.

You can stop and remove all containers by running `sudo docker compose down --rmi all`

Website will be available at [`https://127.0.0.1/`](https://127.0.0.1/)

To test SSL connection self-signed certificates automatically generated when Nginx is deployed.

# Overview
Simple portfolio and a blog built with django and react.

 - **Nginx**: used as a reverse proxy and to serve static files
 - **Database**: Postgres
 - **Cache**: Redis (used for Django Ratelimit)
 - **Auth**: JWT authentication

### **Portfolio main page**

<img src="https://github.com/shogath/portfolio-blog-django-react/blob/main/readme_assets/portfolio.png" width="640" height="360">

### **Pagination**

<img src="https://github.com/shogath/portfolio-blog-django-react/blob/main/readme_assets/pagination.png" width="640" height="360">

### **Contact form**
 - To test contact form I used [Elastic Email](https://elasticemail.com/) because they provide an SMTP server with free account.

 <img src="https://github.com/shogath/portfolio-blog-django-react/blob/main/readme_assets/contact_form.png" width="640" height="360">

### **Blog main page**
 - **Popular posts** are shown based on amount of comments

 <img src="https://github.com/shogath/portfolio-blog-django-react/blob/main/readme_assets/blog.png" width="640" height="360">

 ### **Comments**
 - Only authenticated users can post comments.

<img src="https://github.com/shogath/portfolio-blog-django-react/blob/main/readme_assets/comments_auth.png" width="640" height="360">

<img src="https://github.com/shogath/portfolio-blog-django-react/blob/main/readme_assets/comments.png" width="640" height="360">