# Lab 3

## Team Members

- Shreya Nair github.com/shreyanair614
- May Khan github.com/mayykhan

## Lab Questions

1. Why are RESTful APIs scalable?

	RESTful APIs are scalable because they contain protocols that make it easy to implement and modify it. These protocols include a uniform interface, statelessness (independently executed client requests), and caching that almost eliminates some client-server interactions.
		
2. According to the definition of “resources” provided in the AWS article above, What are the resources the mail server is providing to clients?

	The resources the mail server is providing include all emails stored in a JSON file, "inbox" mail for which the user is the recipient, "sent" mail for which the user is the sender, and a way to pull mail by ID. 

3. What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?

	Our mail server does not have a "put" REST method. If we add one, it could allow the functionality of editing an existing item in our API.
	
4. Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!

	According to AWS, API keys are assigned to first-time clients, who are then permanently authenticated using this key whenever they try to access the server.