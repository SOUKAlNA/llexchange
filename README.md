# llexchange
CSC 3327 Final Project

# Project Overview:
LL-Exchange is an application that allows users to enhance their language skills. Users can initiate a discussion to ask questions about a language. Tutors are types of users that volunteer to register as tutors of a certain language (native language). Tutors can register and answer users’ questions related to their native language or any other language(s) they master.

# Requirements:

## Actors/Roles:
There are four roles/actors.
Clients that will consume the service: the tutor and user.
The administrators: the moderator and admin.

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
