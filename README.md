# GourmetHub

# Introduction
My project is an online restaurant website designed to offer visitors an immersive experience. By showcasing the restaurant's menu, interior ambiance through photos, and operating hours, I aim to assist potential customers in making informed dining decisions. My primary objective is to streamline the reservation process by enabling online bookings and promptly notifying restaurant staff via email. My target users are individuals seeking dining options, and my performance targets include offering an appealing meal selection, facilitating convenient reservation bookings, and ultimately assisting the restaurant in attracting more customers.

## Youtube demo video
### try get  endpoints :[http://pan-gong-blog.us-east-1.elasticbeanstalk.com/actuator](http://pan-gong-blog.us-east-1.elasticbeanstalk.com/actuator)
### or  get all posts : [http://pan-gong-blog.us-east-1.elasticbeanstalk.com/api/posts](http://pan-gong-blog.us-east-1.elasticbeanstalk.com/api/posts)


# AWS Productes Menu Item Requirements
•	List of selected services
Compute – Pick two (2): AWS EC2 , AWS Lambda
Storage – Pick one (1): AWS Relational Database Service (mysql)
Network – Pick one (1): AWS Virtual Private Cloud (VPC), AWS API Gateway
General – Pick two (2) : AWS Backup , AWS SNS
		
•	Comparison of alternative services and why
Compute: I chose AWS EC2 over Elastic Beanstalk due to the greater freedom it offers in managing my application environment.
Storage: For my structured booking information, I selected AWS Relational Database Service (RDS) with MySQL over RDS with NoSQL, as MySQL better suits my data organization needs.

## Deployment Model
I chose a deployment model based on the Public Cloud, primarily because of its popularity and cost-effectiveness. I do not need to buy the infrastructure. I just pay for what I use in deploying the web application.

## Delivery Model
I choose a hybrid delivery model incorporating Infrastructure as a Service (IaaS), Software as a Service (SaaS), and Function as a Service (FaaS). I opted for IaaS as I needed to set up and configure services such as EC2, RDS, and VPC, allowing me to manage and monitor the required software efficiently. Additionally, I leveraged SaaS by utilizing the AWS SNS service for sending notifications to customers, which streamlined communication processes. Furthermore, I integrated FaaS into my delivery model by developing Lambda functions to invoke the SNS service upon user booking, enhancing the responsiveness and scalability of the system.




## The purpose of this project is to learn and practice concepts related to:
- Building a REST API using python django
- refresher Html, css, javascript as front end tech skillss
- practice devops using AWS
- 

During this development, I learned the following concept:
- Python Django web framework
- RESTful API refresher
- HTTP (GET, POST, PUT, PATCH, DELETE, status codes)
- Amazon (Deployment: EC2， RDS, Lambda, SNS)




## The Architecture of the online reservation reasturant:
![Blog API Spring-boot Flow Architecture](![image](https://github.com/panda022/GourmetHub/assets/105373708/9bab6ea5-e224-4e9f-b521-6e9b8b9957bc)

## Data Security Concerns

My web application currently lacks comprehensive data security measures at all layers, leaving it vulnerable to various threats. Potential vulnerabilities include traffic eavesdropping, where attackers could intercept sensitive data transmitted between application and users, and virtualization attacks, which target vulnerabilities in the underlying virtualization infrastructure. I could Implementing Transport Layer Security (TLS), it can encrypt data transmitted between my application and users, preventing unauthorized access to sensitive information.


## Reproducing Architecture in Private Cloud

To replicate my current architecture in a private cloud environment, I would need to invest in a range of hardware and software components. This includes server hardware for hosting my application, database, and other services, along with networking equipment and storage devices. Additionally, I would require licenses for operating systems, database software, and web server software, as well as tools for monitoring and managing my infrastructure. Implementing a private cloud would involve deploying a cloud management platform such as VMware vSphere or OpenStack. Security measures would also need to be implemented, including antivirus software, firewalls, and encryption tools to protect my infrastructure and data. Furthermore, ensuring high-speed internet connectivity and deploying load balancers for traffic distribution are essential. Overall, while the cost estimation can vary based on specific requirements of the hardware, and software. Anyway, it will cost a lot than I use AWS.

## Cost Monitoring

The cloud mechanism that would be most important for me to add monitoring to in order to ensure costs do not escalate unexpectedly would be AWS EC2 instances. Since EC2 instances are the backbone of my application, they have the potential to incur significant costs, especially if I'm not actively monitoring their usage. By implementing monitoring tools for EC2 instances, I can track usage metrics such as CPU utilization, memory usage, and network traffic in real-time. This allows me to identify any instances that are underutilized or experiencing unusually high resource consumption, enabling me to optimize instance sizes, scale capacity as needed, and ultimately prevent unnecessary costs from accumulating.

## Future Development

In the continued development of my application, I plan to focus on enhancing scalability, automation, and security. Key features to be implemented include load balancing for improved performance and reliability, utilizing AWS Elastic Load Balancing (ELB). Furthermore, I aim to introduce Continuous Integration and Continuous Deployment (CI/CD) pipelines with Docker containers, leveraging services like AWS CodePipeline and CodeBuild for automated deployment. Strengthening security measures, I intend to implement authentication and authorization mechanisms for user registration and login. By incorporating these features and utilizing cloud mechanisms effectively, my application will evolve to be more resilient, efficient, and secure in meeting the demands of an ever-changing request.

