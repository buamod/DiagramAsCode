from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.onprem.ci import Jenkins
from urllib.request import urlretrieve
from diagrams.onprem.client import Users

with Diagram("Custom with remote icons", show=True, filename="SecureDome", direction="LR"):

  with Cluster(" Secure Dome"):
    Jenkins("Jenkins")
    stash_url = "https://github.com/buamod/DiagramAsCode/raw/main/assests/stash.png"
    stash_icon = "stash.png"
    urlretrieve(stash_url, stash_icon)
    stash = Custom("Elastic", stash_icon)

  users = Users("Developers")
  users >> stash
  stash - Jenkins