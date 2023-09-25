# Api that allows users to upload images in PNG or JPG format

## 1. Instalation
### 1. Running the project in a Docker Environment

To run this project in a Docker container, follow these steps:

1. **Building the Docker Container:**
   
   Navigate to the project directory where the Dockerfile is located and use this command:

    * ```docker build --tag image_uploader .```
2. Running the Container:
   
    After building the image, you can run the project, mapping ports for accessibility on localhost:

    * ```docker run --publish 8000:8000 image_uploader```

  
  Copy in your browser: http://localhost:8000/ and use the web app :) 

### 2. Second way running the project

  In your cmd navigate to the project directory where the env folder is located.

1. Activate the virtual enviorment
   * On mac:
       *  ```source env/bin/activate```
   * On Windows:
       *  ```.\env\Scripts\activate```

2. Runing the project:
  You can run the project in cmd, using this command:
  ```python3 manage.py runserver```

  Copy in your browser: http://localhost:8000/ and use the web app :)

##  2. Using image_uploader webapp:

1.Admin panel:
    In admin  panel: ```http://localhost:8000/admin/```

  You can perform tasks like adding, editing, and deleting records.
  
1. Api panel:
   In admin  panel: ```http://localhost:8000/api/images``` -  This endpoint allows you to view all images without any user-specific segregation.

  
  In ```http://localhost:8000/api/images/{user.name}``` - Here, {user_name} can be one of the following: **Basic, Premium**, or **Enterprise**. Using this endpoint, you can view images uploaded by a specific user type.







