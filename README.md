# Phone Shop

[View the live project here!](https://phone-shop-python.herokuapp.com/)

**Phone Shop** is a back end Python file, linked to a spreadsheet. The purpose of the Python file is to manipulate the spreadsheet, whenever necessary. The spreadsheet lists the number of phones, by phone type, sold by a shop over the course of a week. It also calculates the surplus and number of stock for each phone type. The sales, surplus and stock are seperated into 3 seperate worksheets, but they are all on one spreadsheet. Each column represents a market day in the week. The numbers in the sales worksheet represents the number of each phone type sold on each market day.

### Sales Worksheet
![An image of the Sales worksheet](assets/images/Sales%20worksheet.png)

### Surplus Worksheet
![An image of the Surplus worksheet](assets/images/Surplus%20worksheet.png)

### Stock Worksheet
![An image of the Stock worksheet](assets/images/Stock%20worksheet.png)

## Features

The user can use the program to manipulate the spreadsheet in any way they see fit. The user is prompted to input their values below the 'Enter your data here:'. This enables them to add data values to the relevant worksheet, which will add rows of data into the worksheet. The program will then perform the necessary calculations that will produce the new surplus. The user can also press the 'run program' button at any point to restart the program, if they have entered incorrect data values but have not ran the program yet.

![An image of the Python program](assets/images/Python%20Program.png)


## Testing

In order to ensure the program ran smoothly with the spreadsheet, it was tested by inputting random data values. In order for a test to be successful, the data values should be added as rows to the Sales worksheet and this will then result in a new row of calculated values in the Surplus worksheet.

## Validator Testing

To ensure the Python program ran smoothly and had no errors, it was tested for validation. Testing for the code and more information on how it was tested are explained below in more detail.

1. Python program 
-  Warning messages did occurr, in relation to indentation and whitespaces. However, no errors were found when running the Python code on the [PEP8 online check](http://pep8online.com/)


## Unfixed Bugs

One unfixed bug that occurred was calculating the stock numbers through the program the same way as the surplus. When inputting the sales data values, the program should calculate the surplus and stock number accordingly. This is the case for the surplus numbers. However, the terminal throws an error message in regards to the stock numbers. The code was obtained from the Code Institute Source Code, along with walkthough videos for guidance. Regardless of this, the stock numbers were not calculated. In future, more in-depth research and debugging will be conducted in order to prevent issues like this from occuring. Below are two screenshots of the terminal when running the program. The first shows the error message that occurs and the second is what the program should do when running the code.

### Unfixed Bug - My Result
![An image of the unfixed bug](assets/images/Unfixed%20bug%20-%20my%20result.png)

### Sales Worksheet
![An image of the solution to the unfixed bug](assets/images/Unfixed%20bug%20-%20solution.png)

## Deployment

The website was deployed to Heroku. To successfully deploy a website, follow the steps below:

1. Go to the [Heroku website](https://www.heroku.com/).
2. Sign up for a Heroku account, fill out your personal details and follow the link sent to your email to create your account.
3. Accept their terms of service and this will direct you to your dashboard.
4. Click on 'Create a new app'.
5. Give your app/website a name in the 'App name' option, choose a region and then click 'create app'.
6. Click on the settings tab.
7. Click on the 'Reveal Config Vars' button.
8. You will be asked to enter a 'KEY' and 'VALUE' (steps 9 and 10 are only necessary if your website has a JSON file).
9. If you have a JSON file, enter its name in all caps in the 'KEY' field.
10. Copy the entire JSON file and enter. its contents in the 'VALUE' field.
11. Click Add to add this key/value pair.
12. Enter PORT in the 'KEY' field.
13. Enter 8000 in the 'VALUE' field.
14. Click Add to add this key/value pair.
15. Scroll down to the 'Buildpacks' section.
16. Click the Add buildpack button.
17. Select the Python buildpack and then click save changes.
18. Click the Add buildpack button.
19. Select the 'nodejs' buildpack and click save changes.
20. Ensure the buildpacks are in the order that the Python buildpack is on top and 'nodejs' underneath.
21. Scroll to the top of the page and click the deploy tab.
22. Select Github as the deployment method.
23. Click Connect to GitHub and sign into your GitHub account, if required.
24. Search for your GitHub repository name.
25. Click search and then connect to link the Heroku app to the GitHub repository code.
26. Select the Manual deploy option by clicking on the button: Deploy Branch.
27. Wait for the app to be built (a message will appear saying your app was successfully deployed).
28. Click the View button.
29. This will take you to your deployed link.

The link to the live website can be found [here](https://phone-shop-python.herokuapp.com/)


## Credits

Below, any references used as help have been listed below. References include : code from other respositories, video tutorials, external websites and images. 

### Content

- The video tutorials provided by Code Institute were used as a base structure for the entire project, along with their source codes.
- The source code for the [Home Page](https://github.com/Code-Institute-Solutions/love-running-2.0-sourcecode/blob/main/08-responsive-elements/05-responsive-gallery/index.html)
- The source code for the [Gallery Page](https://github.com/Code-Institute-Solutions/love-running-2.0-sourcecode/blob/main/08-responsive-elements/05-responsive-gallery/gallery.html)
- The source code for the [CSS](https://github.com/Code-Institute-Solutions/love-running-2.0-sourcecode/blob/main/08-responsive-elements/05-responsive-gallery/assets/css/style.css)
- The fonts used for the entire project were obtained from [Google Fonts](https://fonts.google.com/)
- The icons used in the project were obtained from [Font Awesome](https://www.fontawesome.com/)
- The script code, located at the bottom of each HTML file, was obtained from my kit, after creating an account on [Font Awesome](https://fontawesome.com/kits/749939eb6c/use)

### Media 

- The images used for this website were taken from [Pexels](https://www.pexels.com/)
- Image [hero-image](https://www.pexels.com/photo/man-lifting-barbel-17840/) taken from Pexels
- Image [ethos-center-image](https://www.pexels.com/photo/man-holding-barbell-1431282/) taken from Pexels
- Image [times-background](https://www.pexels.com/photo/bridge-over-river-in-city-258117/) taken from Pexels

The following images obtained from [Pexels](https://www.pexels.com/) were used in the Gallery page: 

1. [Man sitting on a flat bench](https://www.pexels.com/photo/man-sitting-on-flat-bench-3490348/)
2. [Woman doing sit ups](https://www.pexels.com/photo/woman-doing-sit-ups-3076516/)
3. [Man curling dumbbell](https://www.pexels.com/photo/man-in-white-tank-top-and-grey-shorts-lifting-dumbbell-3838389/)
4. [Woman raising dumbbell ](https://www.pexels.com/photo/photo-of-woman-sitting-and-raising-dumbbells-2475875/)
5. [Man bench pressing](https://www.pexels.com/photo/muscular-sportsman-training-with-heavy-barbell-during-weightlifting-workout-in-modern-gym-3837781/)
6. [Man doing shoulder press with dumbbells](https://www.pexels.com/photo/man-exercising-at-a-gym-4164759/)
7. [Man doing push ups](https://www.pexels.com/photo/photo-of-man-doing-push-ups-using-yellow-kettlebell-4720269/)
8. [Woman using elliptical machine](https://www.pexels.com/photo/exhausted-young-obese-woman-training-on-elliptical-machine-with-support-of-asian-male-instructor-6551093/)
9. [Man deadlifting](https://www.pexels.com/photo/man-lifting-a-barbell-4720776/)

## Acknowledgements

- I would like to thank my mentor for his full support and help throughout this project.