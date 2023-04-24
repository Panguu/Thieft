# Thieft

A Bluetooth Enabled Anti-Theft device for vehicles.




This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Installation
### Raspberry Pi
#### dependencies;
- ppp
- minicom
- python3
- python3-smbus
- python-pip
- crontab
#### pip dependencies:
- pybluez
- mpu6050-raspberrypi

#### Step 1
After cloning the project move the src/raspberryPiCode directory to the raspberry pi
and open the directory.

```
chmod 755 launcher.sh
```
this gives the launcher script root permissions if not already set. launching the launcher.sh from now on should run the program
#### Step 2
If you wish to have the thieft detection run on device startup we recommend creating a logs directory using;
```
mkdir logs
```
This is to keep track of any logs or incidents that may occur.
#### Step 3
```
@reboot sh /path/to/launcher.sh >/path/to/logs/directory/logs/cronlog 2>&1
```
this will create a cronlog file on next start up and will keep track how the project is running

### Server
#### dependencies;
- python3
- npm
- nodejs
#### pip dependencies:
- django

#### Step 1
Running the server requires having all the above dependencies installed. 
You can change directory into the src/thieft/frontend/ and run npm i to install the node models required for the server
#### Step 2 
After installing the node modules you can run npm run build to build the static files that will be used by django to run the web server.
#### Step 3
Once the build script has finished you can change directory back into the thieft directory and run 
```
python manage.py runserver
```
## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
