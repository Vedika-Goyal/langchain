from langchain_community.tools import DuckDuckGoSearchRun,ShellTool
search_tool=DuckDuckGoSearchRun()
results=search_tool.invoke('ipl news')
print(results)
shell_tool=ShellTool()
results2=shell_tool.invoke('whoami')
print(results2)