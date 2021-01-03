# llexchange
CSC 3327 Final Project

# Project Overview:
LL-Exchange is an application that allows users to enhance their language skills. Users can initiate a discussion to ask questions about a language. Tutors are types of users that volunteer to register as tutors of a certain language (native language). Tutors can register and answer users’ questions related to their native language or any other language(s) they master.

# Requirements:

## Actors/Roles:
There are four roles/actors:
- Clients that will consume the service: the tutor and user.
- The administrators: the moderator and admin.

## 1.	Functional Requirements:

### User:
-	A user is able to choose the language in which they view the platform.
-	A user is able to register and create an account.
-	A user is able to search for a target language.
-	A user is able to browse all tutors of the target language. 
-	A user is able to display a tutor’s profile.
-	A user is able to display all other user’s questions or discussions in a language.
-	A user is able to ask a question.
-	A user is able to start a discussion under their own question post.
-	A user is able to rate a tutor’s skills in a certain language.
-	A user is able to rate the answer of a tutor.
-	A user is able to report a tutor’s messages to the moderators.
-	A user is able to report a user’s messages to the moderators.
-	A user is able to block a tutor from further messaging them.
-	A user is able to close a discussion they have started.

### Tutor:
-	A tutor is able to choose the language in which they view the platform.
-	A tutor is able to register and create an account.
-	A tutor is able to create a profile with relevant information and descriptions.
-	A tutor is able to search for a target language.
-	A tutor is able to display all user’s questions or discussions in a language.
-	A tutor is able to reply to a user’s question or discussion.
-	A tutor is able to report a user’s messages to the moderators.
-	A tutor is able to report a tutor’s messages to the moderators.

### Moderator:
-	A moderator is able to choose the language in which they view the platform.
-	A moderator is able to choose the languages they shall moderate in. 
-	A moderator is able to receive reports from users and tutors along with the flagged messages for review.
-	A moderator is able to display all open and closed questions or discussions of users in the language they moderate in.
-	A moderator is able to suspend a user or tutor in case of transgression of terms and rules of usage.
-	A moderator is able to close a discussion started by a user.
-	A moderator is able to delete a question or discussion started by user in case of transgression of terms and rules of usage.
-	A moderator is able to delete a tutor’s reply in case of transgression of terms and rules of usage.
-	A moderator is able to delete a user’s reply in case of transgression of terms and rules of usage.

### Admin:
-	A default admin is created automatically.
-	An admin is able to choose the language in which they view the platform.
-	An admin is able to create other admin and moderator accounts.

## 2.	Non-functional Requirements:

### Performance: 
The system shall be able to score a 70% or above on web vitals metrics. 

### Scalability: 
The system shall be able to preserve performance and accommodate increase of load. 

### Security: 
-	The confidentiality, integrity and availability of the data stored and transferred shall be ensured.
-	Communications between users and tutors shall be moderated (automatically or when needed reviewed by a moderator). 
-	User’s access shall be restricted to their own account and messages.
-	Tutor’s access shall be restricted to their own account and messages.
-	Moderator’s access shall be restricted to their own account and reported messages.
-	Users and tutors shall be asked to provide verified email addresses. 
-	Service high availability shall be ensured, i.e., no single point of failure (SPoF) shall be accepted.


# Project Architecture:

## Techonologies:
The language of implementation of this project will be Python. To isolate dependencies, the tool Virtualenv shall be used to create a Python environment. The chosen framework is Django, which also supports its own ORM; Django ORM. 

## Physical Architecture- Initial:
The architecture is a multi-tier architecture along with a firewall for security and an external server to enforce the email validation requirement. 
 
## Physical Architecture- Protocol & Software:
The webservice protocol that will be used is REST. HTTPS will also be used to enforce security of data transfer. The database will be managed using PostgreSQL.
 
## Physical Architecture- Resilient (No SPoF)/ Scalability:
To enforce the No SPoF and high availability requirements, reverse proxying Nginx servers will be implemented with added load balancing feature. There will be a cluster of load balancers, which will be configured using Linux HA, as well as a cluster of application and database servers.  
 
## Logical Architecture- Inside an Application Server:
The representation below exemplifies the MVC architecture and gives a closer look to the logical structures and frameworks inside each application server.


# Project Design:

## Class Diagram:

### Entity Class Diagram:
-	I have separated the administrative users from the other users that consume services, as the latter are the only type of users that have a profile.
-	The rating entity is related to profile as users can rate tutors and the rating is computed and kept track of.
-	The message entity has a recursive relation with itself, as there are two subcategories of messages, the main message (header of the discussion) and its replies.
-	A message is posted by a user or tutor. 
-	The relation between the language entity and the message entity is that of 1...n, as each language will have messages/discussions under it. 
-	Each languages has one or many moderators and tutors attributed to it. 
 
### Services Class Diagram:

There are three services: 

- The rating service that has as logical method that computes the average rating of each tutor as users enter new ratings, and updates the rating of the tutor. 
- The user service that takes care of logging in and out users, identifying the type of the user, authority and permissions.
- The discussion service that takes care of reporting users and tutors, checking if the tutor is blocked before being allowed to post.
 
## Sequence Diagram:

### Data-driven Sequence Diagram:
For a data-driven operation, the Json file in the request’s body of the user is parsed and deserialized (translated) to form an object. If the object’s attributes are valid it can be saved and mapped to a model (i.e.: in case of a create or update). Then either a response is returned or in case of a GET request, the framework serializes the object. The rendered Json file is then returned to the user. 
Serializer is a class in django’s rest framework API.

### Service-driven Sequence Diagram:
The following diagram represents how a REST request from a client propagates forward and backward through the layers. When a request is received through a REST controller (in the case of django, a view), the deserializition forms the object which is then passed to the appropriate service. The service calls on the model and performs its logical operations. The service returns either a response or an object, in which case it is serialized and rendered into a Json file before getting returned to the client.
s
