from diagrams import Cluster, Diagram
from diagrams.onprem.ci import Jenkins
from diagrams.generic.os import Ubuntu
from diagrams.onprem.client import Users
from urllib.request import urlretrieve
from diagrams.custom import Custom


with Diagram("Simple Web Service with DB Cluster", show=False):
    developers = Users("Dev")

    stash_url = "https://github.com/buamod/DiagramAsCode/raw/main/assests/stash.png"
    stash_icon = "stash.png"
    urlretrieve(stash_url, stash_icon)
    stash = Custom("Elastic", stash_icon)

    with Cluster("Agents pool"):
        agents = [
            Ubuntu("agent01"),
            Ubuntu("agent02"),
            Ubuntu("agent03")]

    with Cluster("Jenkins Main Node"):
        jenkins = Jenkins("jenkins")

    with Cluster("Multibranch Pipeline"):
        jenkins = Jenkins("jenkins")

    developers >> stash >> jenkins >> agents