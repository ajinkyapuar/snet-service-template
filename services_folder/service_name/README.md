[issue-template]: ../../../../../issues/new?template=BUG_REPORT.md
[feature-template]: ../../../../../issues/new?template=FEATURE_REQUEST.md

![singnetlogo](../../docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')

# {{SERVICE_DOCS_TITLE}}

{{SERVICE_DOCS_INTRO}}

It is part of our [{{REPOSITORY_TITLE}}](https://github.com/{{GITHUB_ACCOUNT}}/{{GITHUB_REPOSITORY}}).

## Getting Started

### Requirements

- [Python 3.6.5](https://www.python.org/downloads/release/python-365/)
- [Node 8+ w/npm](https://nodejs.org/en/download/)

### Development

Clone this repository:

```
$ git clone https://github.com/{{GITHUB_ACCOUNT}}/{{GITHUB_REPOSITORY}}.git
$ cd {{SERVICES_FOLDER}}/{{SERVICE_NAME}}
```

### Running the service:

To get the `ORGANIZATION_NAME` and `SERVICE_NAME` you must have already published a service 
(check this [link](https://github.com/singnet/wiki/tree/master/tutorials/howToPublishService)).

Create the `SNET Daemon`'s config JSON file (`snetd.config.json`).

```
{
   "DAEMON_END_POINT": "DAEMON_HOST:DAEMON_PORT",
   "ETHEREUM_JSON_RPC_ENDPOINT": "https://kovan.infura.io",
   "IPFS_END_POINT": "http://ipfs.singularitynet.io:80",
   "REGISTRY_ADDRESS_KEY": "{{REGISTRY_ADDRESS}}",
   "PASSTHROUGH_ENABLED": true,
   "PASSTHROUGH_ENDPOINT": "SERVICE_GRPC_HOST:SERVICE_GRPC_PORT",  
   "ORGANIZATION_NAME": "ORGANIZATION_NAME",
   "SERVICE_NAME": "SERVICE_NAME",
   "LOG": {
       "LEVEL": "debug",
       "OUTPUT": {
            "TYPE": "stdout"
           }
   }
}
```

For example:

```
$ cat snetd.config.json
{
   "DAEMON_END_POINT": "http://{{SERVICE_DAEMON_HOST}}:{{SERVICE_DAEMON_PORT}}",
   "ETHEREUM_JSON_RPC_ENDPOINT": "https://kovan.infura.io",
   "IPFS_END_POINT": "http://ipfs.singularitynet.io:80",
   "REGISTRY_ADDRESS_KEY": "{{REGISTRY_ADDRESS}}",
   "PASSTHROUGH_ENABLED": true,
   "PASSTHROUGH_ENDPOINT": "http://localhost:7003",
   "ORGANIZATION_NAME": "{{ORGANIZATION_NAME}}",
   "SERVICE_NAME": "{{SERVICE_NAME}}",
   "LOG": {
       "LEVEL": "debug",
       "OUTPUT": {
           "TYPE": "stdout"
           }
   }
}
```
Install all dependencies:
```
$ pip3 install -r requirements.txt
```
Generate the gRPC codes:
```
$ sh buildproto.sh
```
Start the service and `SNET Daemon`:
```
$ python3 run_{{SERVICE_FILE_NAME}}_service.py
```

### Calling the service:

Inputs:
  {{SERVICE_INPUT_DESCRIPTION_LIST}}

Local (testing purpose):

```
$ python3 test_{{SERVICE_FILE_NAME}}_service.py
{{SERVICE_TEST_SCRIPT_CONSOLE_INPUTS}}

{{SERVICE_TEST_SCRIPT_CONSOLE_OUTPUTS}}
```

  {{SERVICE_OUTPUT_DESCRIPTION_LIST}}

For further instructions about the output of this service, check the [User's Guide](../../docs/users_guide/{{SERVICES_FOLDER}}/{{SERVICE_NAME}}.md).

Through SingularityNET (follow this [link](https://github.com/singnet/wiki/blob/master/tutorials/howToPublishService/README.md) 
to learn how to publish a service and open a payment channel to be able to call it):

Assuming that you have an open channel (`id: 0`) to this service:

```
$ {{SERVICE_SNET_CALL_COMMAND}}
unspent_amount_in_cogs before call (None means that we cannot get it now):1
{{SERVICE_SNET_CALL_RESPONSE}}
```

## Contributing and Reporting Issues

Please read our [guidelines](https://github.com/singnet/wiki/blob/master/guidelines/CONTRIBUTING.md#submitting-an-issue) before submitting an issue. 
If your issue is a bug, please use the bug template pre-populated [here][issue-template]. 
For feature requests and queries you can use [this template][feature-template].

## Authors

* **{{AUTHOR_FULLNAME}}** - *Maintainer* - [SingularityNET](https://www.singularitynet.io)