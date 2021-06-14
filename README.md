# shopping-cart

# Instructions

  1. Visit the datright's ["shopping-cart" repository](https://github.com/datright/shopping-cart), which contains a simple command-line application. 

  2. Click "Fork" to copy the repo under your own control. 

  3. Follow the instructions in the repository's "README.md" file to install, setup and run the Python code contained inside:

     a. Use your Git client to "clone" (download) the remote fork onto your local machine 

     b. Use the command-line to navigate into the local repository:
     ```sh
     cd shopping-cart
     ```

     c. Use the `conda` utility to create a new virtual environment with the latest version of Python, then activate it: 
     ```sh
     conda create -n shopping-env python=3.8
     conda activate shopping-env
     ```

     d. Use the `pip` utility to install required third-party package specified in the repo's "requirements.txt" file, which in this case is "python-dotenv" 
     ```sh
     pip install -r requirenments.txt
     ```

     e. Use a ".env" file approach to set an environment variable to customize the tax rate and email address that the receipt will be sent from. You can customize the user name by typing 
     ```
     PLAYER_NAME=tax rate of your jurisdiction 
     SENDGRID_API_KEY=API key from SendGrid
     SENDER_ADDRESS=your email address
     ```

     f. Use the `python` utility to run the Python file(s)
     ```
     python shopping_cart.py
     ```