#get total amount of productivity in last 7 days

from toggl.TogglPy import Toggl
toggl = Toggl()

toggl.setAPIKey('53a2d3c3856e1ef39982074936cd0c51')

response = toggl.request("https://toggl.com/reports/api/v2/weekly")

print(response)
