# auto-attendance
Automated attendance recording tool for Moodle built using Selenium.

### For individuals

The file [individual.py](https://github.com/aswinmprabhu/auto-attendance/blob/master/individual.py) contains the script for automatic attendance marking for one individual as shown in the above tutorial. All configuration is to be done within that single file.

To run the script,

1. Clone the repository using the git command `git clone https://github.com/aswinmprabhu/auto-attendance.git`
2. Ensure that python3 and pip3 are installed
3. Download and place the chromedriver file in the repository folder
4. Edit the individual.py file
    * Modify the `moodle_mail` and `moodle_pass` variables with your credentials
    * Change the chromedriver file location and name if necessary (OS dependent)
    * Edit the `attendance_page_urls` variable with the URLs to all the attendance pages of your subjects
5. Inside the repository folder, execute the following commands
```bash
pip install selenium
python3 ./individual.py
```
(Try using pip3 is pip command does not work)

### For groups of individuals

The file [attendance.py](https://github.com/aswinmprabhu/auto-attendance/blob/master/attendance.py) contains the script for automatic attendance recording for a group of individuals. A separate config file called `config.json` needs to be created for this to work.

To run the script,

1. Clone the repository using the git command `git clone https://github.com/aswinmprabhu/auto-attendance.git`
2. Ensure that python3 and pip3 are installed
3. Download and place the chromedriver file in the repository folder
4. Create a config.json file inside the repository folder. A sample file is given below.
```javascript
{
	"driver": "./chromedriver.exe",
	"interval": 20,
	"users": [
		{
			"name": "user1",
			"email": "email1@mec.ac.in",
			"password": "pass1",
			"courses": [
				"http://moodle.mec.ac.in/mod/attendance/view.php?id=9022",
				"http://moodle.mec.ac.in/mod/attendance/view.php?id=9002",
			]
		},
		{
			"name": "user2",
			"email": "email2@gmail.com",
			"password": "pass2",
			"courses": [
				"http://moodle.mec.ac.in/mod/attendance/view.php?id=9027",
				"http://moodle.mec.ac.in/mod/attendance/view.php?id=9129",
			]
		}
	]
}
```
5. Make the necessary edits to config.json. Change the driver location if necessary and edit the user details. You can add more users by appending to the `users` array in the config.
6. Inside the repository folder, execute the following commands
```bash
pip install selenium
python3 ./attendance.py --config ./config.json
```

Please visit [MY BLOG](https://aswinmprabhu.netlify.app/posts/automating-attendance-recording-on-moodle-using-selenium/) for better understanding of this project.

(Try using pip3 is pip command does not work)
