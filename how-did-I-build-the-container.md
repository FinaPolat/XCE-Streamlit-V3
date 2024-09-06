### How did I build the container?

1. Create the Dockerfile.
2. Build the image
``` docker build -t xce-streamlit_v3 .  ```
3. Run it to check if it works.
``` docker run -p 8501:8501 -e HUGGINGFACEHUB_API_TOKEN -v C:\Users\fyilmaz\Desktop\xce-streamlit-v3\my_class_expression.json:/app/class_expression.json xce-streamlit_v3 ```
4. Log in to Docker Hub.
``` docker login ```
5. Tag the image.
``` docker tag xce-streamlit_v3 finapolat/xce-streamlit_v3:enexa ```
6. Push the image. 
``` docker push finapolat/xce-streamlit_v3:enexa ```