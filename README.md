# HTTPS_PYTHON_SERVER
This is a simple encrypted python server that handles GET and POST requests.


---
## DESCRIPTION
The basic HTTPS web-server application listens on a configurable TCP port and serves both static HTML and dynamically generated HTML. 
Due to safety policies, the security key and certificate were not pushed to the repository. 
To obtain a security key/certificate pair, download openSSL through the link: https://www.openssl.org/source/gitrepo.html and write your certificate. 
Copy the security key and paste it just below the certificate key (in the same file)


---
## RUNNING THE SERVER
Download the zip file from the repo and unzip it to your preferred location.
Open the command prompt/shell and change the file directory to where the script sits.
Run the script by: python scriptName.py.
Copy and paste the localhost IP Address on the command prompt.
If the site is blocked by the browser, go to advanced settings and click on proceed anyway.
By default, the server returns an index.html page if it sits in the same directory. Otherwise, the directory where the script sits is opened through the browser.




---
## CREDITS
Alex Kagozi


---
## LICENSE AND COPYRIGHT
Copyright &copy; Alex Kagozi

## SCREENSHOT
![httpsserver (2)](https://user-images.githubusercontent.com/70429029/150094861-123ccaf4-8b99-4ea0-98ff-4b02b00e6536.png)
