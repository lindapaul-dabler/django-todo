import boto3
client = boto3.client('ecs')

def create_ecs_cluster(cluster_name):
    client = boto3.client('ecs')
    response = client.create_cluster(
        clusterName=cluster_name
    )
    print("ECS cluster created:", response['cluster']['clusterArn'])

def create_fargate_task():
    client = boto3.client('ecs')
    response = client.run_task(

        cluster='my-ecs-cluster',

        launchType = 'FARGATE',

        taskDefinition="my-task-definition",

        count = 1,

        platformVersion='LATEST',

        networkConfiguration={

                'awsvpcConfiguration': {

                    'subnets': [

                        'subnet-02107846e092a3245',

                        'subnet-0924c8e32dd336f17',

                        'subnet-0ebf7e7dc4289c7e6'

                    ],

                    'assignPublicIp': 'ENABLED'

                }

            },

            overrides={

                
                'containerOverrides': [
                   {

                    'environment': [], 
                        
                        "name": "my-container",
                        "image": "my-namespace/my-image",
                        "cpu": 10,
                        "memory": 500,
                "portMappings": [
            {
                "containerPort": 8080,
                "hostPort": 80
            }

#
 #                           {

 #                               'name': 'pipelineid',

#                                'value': str(pipelineid)

 #                           },

  #                          {

   #                             'name': 'pipelinename',

    #                            'value': pipelinename

     #                       },

      #                      {

       #                         'name': 'stepid',

        #                        'value': str(stepid)

         #                   },

          #                  {

           #                     'name': 'stepname',

            #                    'value': stepname

             #               },

              #              {

               #                 'name': 'repopath',

                #                'value': repopath

                 #           },

                  #          {

                   #             'name': 'GIT_USERNAME',

                    #            'value': username

                     #       },

                      #      {

                       #         'name': 'GIT_PASSWORD',

                        #        'value': password

                         #   },

                          #  {

                           #     'name': 'entrypoint',

                            #    'value': entrypoint

                            #},

                           # {

#                                'name': 'executionid',

 #                               'value': str(executionid)

  #                          },

   #                         {

    #                            'name': 'executionstepsid',

     #                           'value': str(executionstepsid)

      #                      },

       #                     {

        #                        'name': 'onerroraction',

         #                       'value': onerroraction

          #                  },

           #                 {

            #                    'name': 'parallelid',

             #                   'value': str(parallelid)

              #              },

               #             {

                #                'name': 'parallelism',

                 #               'value': str(parallelism)

                  #          },

                ]

                    }

                ]

            }    

        )
    
    print("Fargate task created:", response['tasks'][0]['taskArn'])

# Usage
cluster_name = 'my-ecs-cluster'
#task_name = 'my-fargate-task'
#task_definition = 'my-task-definition:1'
#subnet_ids = ['subnet-12345678', 'subnet-87654321']
#security_group_ids = ['sg-12345678']
create_ecs_cluster(cluster_name)
create_fargate_task()
