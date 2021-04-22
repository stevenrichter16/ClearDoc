# ClearDoc, an AI-powered doctor's assistant for simplifying medical terminology

## Demo: https://youtu.be/U7bLF-driH0?t=298 at timestamp 4:58

### Credits
Front-end (React.js) / Back-end (Flask): **Steven Richter** | stevenrichter16@gmail.com

Styling (CSS/SCSS): **Tim Uster** | timuster@live.com

GPT-3 Prompt Engineering: **Alan Majer** | alanmajer@hotmail.com ||
                          **Matthew Donaruma** | matt@mdonaruma.com

### What/Why?
The motivation for this application came from recognizing the dense and confusing nature of clinical notes and medical terminology With the use of GPT-3, a deep learning model developed by OpenAI, my OpenAI/NextGrid hackathon team surmized the concept of an application that translates medical lingo into simple English. This application/assistant provides patients a better overall clinical experience.  

### Development Process

Over the course of 8 hours I created the front-end and back-end from scratch, only having moderate knowledge of React.js, and minimal knowledge of Flask. Through much trial and error I accomplished setting up a REST API with Flask.

The main issue I encountered in creating the API centered around the POST method. Previously I used Flask to set up a GET endpoint, but I had never developed an API a POST endpoint wherein the client could send user data to the server to have it processed, then back to the client. The need for this functionality came from the need to grab user input from the client, send it to the Python server, process it through the GPT-3 API, then send that data back to the client to be displayed. The majority of the development time spent consisted of fixing errors with the POST method. Once I succeeded in writing the POST method I realized how simple it was in hindsight.

### Conclusion

Overall this project gave me experience in full-stack web development, and sharpened my communication skills. Since this application is a demo, it is not developed to its fullest potential. In the future this application could be used by doctors and nurses across English speaking countries, and additional language options could be added. We think this AI assistant highlights the nascence of AI-powered health services, of which will revolutionize the field of medicine.  

A url for this web application will be available soon. Here is the slide deck for the presentation we gave during the hackathon: https://docs.google.com/presentation/d/1lIQbtUXYoazawjZ-VRQ_8Shp3e8G37gkbUy-jFxrqlI/edit?usp=sharing

Disclaimer: If you run the project from the source files it will not work since it requires me to reveal my GPT-3 API key. I am working to fix that, and a demo of this app is located at the top of this document.
