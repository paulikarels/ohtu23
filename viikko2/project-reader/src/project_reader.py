from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        tomli_dict = tomli.loads(content)
        #print(tomli_dict)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
                tomli_dict.get("tool").get("poetry").get("name"), 
                tomli_dict.get("tool").get("poetry").get("description"), 
                tomli_dict.get("tool").get("poetry").get("license"), 
                tomli_dict.get("tool").get("poetry").get("authors"), 
                tomli_dict.get("tool").get("poetry").get("dependencies"), 
                tomli_dict.get("tool").get("poetry").get("group").get("dev").get("dependencies")
            )
