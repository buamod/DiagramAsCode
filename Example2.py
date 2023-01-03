from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.ci import Jenkins
from diagrams.generic.os import Ubuntu
from diagrams.onprem.client import Users
from diagrams.onprem.client import User
from urllib.request import urlretrieve
from diagrams.custom import Custom
from diagrams.oci.monitoring import Workflow
from diagrams.saas.identity import Okta
from  diagrams.oci.database import DataflowApache

with Diagram("Simple Web Service with DB Cluster", show=False):
    developers = Users("Dev")
    access = User("access")

    stash_url = "https://github.com/buamod/DiagramAsCode/raw/main/assests/stash.png"
    stash_icon = "stash.png"
    urlretrieve(stash_url, stash_icon)
    stash = Custom("Elastic", stash_icon)

    with Cluster("Agents pool"):
        agents = Ubuntu("agent01") - \
        Edge(color="brown", style="dotted") \
        - Ubuntu("agent02") - \
        Edge(color="brown", style="dotted") \
        - Ubuntu("agent03")

    with Cluster("Jenkins Main Node"):
        saml = Okta("SAML 2.0")
        jenkins = Jenkins("jenkins")
        saml >> jenkins

    with Cluster("Multibranch Pipeline"):
        maven_url = "https://github.com/buamod/DiagramAsCode/raw/main/assests/maven.png"
        maven_icon = "maven.png"
        urlretrieve(maven_url, maven_icon)
        maven = Custom("Build", maven_icon)

        branch = Workflow("branch")
        promote = DataflowApache("promote")
        branch - maven >> Edge(color="darkgreen") >> promote

    access >> saml
    developers >> stash >> jenkins >> agents >> Edge(color="darkorange") >> maven