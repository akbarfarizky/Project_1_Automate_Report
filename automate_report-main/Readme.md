# Dashboard Automation

Goal :
1. Monthly Sales Data as output
2. Send to Slack channel (a team collaboration platform)
3. Teams can view regular monthly reports

Steps :
1. 'pip install -r requirements. txt`
2. Create a `.env` file inside the `plugins/send_to_slack` directory
3. Fill in `.env` with the following content SLACK_TOKEN='your-slack-token'
4. Run `python report.py` to send the graph to the Slack Channel

Problems :

For MAC dan Linux user :
1. If your device is MAC or Linux and you see Python not found, try running the following command:
     `which python` or `which python3`
2. Then check whether the path directory is already in the PATH environment variable by:
     `echo $PATH`
3. If it's not there, add it by `export PATH=$PATH:/path/to/python`

Windows :
1. https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows
