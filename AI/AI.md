# AI

The goal of software engineering in the AI era is to manage the AI loop with an effective harness. We create a specification for the AI to follow. We give it guidelines for how to achieve the goal. The focus remains on the goal of turning ideas into outcomes: making useful software.

## Resources

### Using GPT-6

https://developers.openai.com/api/docs/guides/latest-model

The new models are much better at following directions. The default of the model is to be a question-asking, professional and detailed response, test making slow and thorough worker. You can modify this behavior with the custom prompts given in the guide: Speak plainly, delegate work, limit tests, and follow-throuhg with best judgement.

### Building effective agent automations

https://claude.dev/blog/building-effective-agent-automations/

A tutorial article and overview on building agent automations, with a marketing plug for Claude Managed Agents. It integrates with Slack and Github.

Simple agent automations are used to help manage increasing AI workload. These automations run on a schedule, gather data from sources, and tell humans what we need to know.

The code contains a reference implementation and installation and quickstart instructions.

The system is brokend down into these parts: 
- Sources
- Schedule
- Agent
- Memory
- Destination
- Reader

The sources are slack channels and Github pull requests.

The agent has its own, scoped credentials. Claude uses vaults. 

The agent calls Github MCP, and Slack API on shell with curl.

The system uses ant cli. 

You create the vault and add each credential through typescript one-off script. 

Then you copy vault ID from claude-lock.json into vault_ids in deployment.md

The agent timestamps runs and stores them in memory. It can also store the last run time in a file.


## Unlimited Tokens

The best token deals right now: 

Muse Spark 1.3 Contributor: 48 on artifical analaysis, 81.6 on LiveBench. Use on OpenCode Go. 

Z.ai GLM-5.3 Flash: Almost billions of tokens per week using off-peak hours. 42 on artifical analysis, 71.6 on LiveBench. Use on ZCode.

Opencode Go: Unlimited models temporarily come and go. May get unlimited usage through Zen API.

Featherless: Unlimited tokens with rate limits, may be nice.