import random


user_input = -1
while user_input != 0:
	
	phone_start = """

	NOKIA
	Select a number
	1 >>> Phone Book
	2 >>> Messages
	3 >>> Chat
	4 >>> Call Register
	5 >>> Tones
	6 >>> Settings
	7 >>> Call Divert
	8 >>> Games
	9 >>> Calculator
	10 >>> Reminders
	11 >>> Clock
	12 >>> Profiles
	13 >>> SIM Services
	0 >>> Phone Off

			"""

	print(phone_start)
	user_input = int(input("your choice: "))
	
	match user_input:

		case 1: 
			new_user_input1 = 1
			while new_user_input1 != 0:

				phonebook = """

				Phone Book
				Select a number
				1 >>> Search
				2 >>> Services Nos.
				3 >>> Add Name
				4 >>> Erase
				5 >>> Edit
				6 >>> Assign Tone
				7 >>> Send B'card
				8 >>> Options
				9 >>> Speed Dials
				10 >>> Voice Tags
				0 >>> Back

						"""
				
				print(phonebook)
				new_user_input1 = int(input("your choice: "))

				match new_user_input1:
		
					case 1: 	
		
						new_user_input1_1 = -1
						while new_user_input1_1 != 0:
		
							search = """

							Search
							0 >>> Back

								"""

							print(search)
							new_user_input1_1 = int(input("your choice: "))
					
							match new_user_input1_1:
								
								case _: 
									if new_user_input1_1 != 0:  print("Invalid Input! Try Again..")

							
				
						#Search while loop ends
						


					case 2: 	

						new_user_input1_2 = -1
						while new_user_input1_2 != 0:
		
							servicesNos = """

							Services Nos.
							0 >>> Back

								"""

							print(servicesNos)
							new_user_input1_2 = int(input("your choice: "))
					
							match new_user_input1_2:
								
								case _: 
									if new_user_input1_2 != 0:  print("Invalid Input! Try Again..")
							
				
						#Services Nos while loop ends
						

					
					case 3:		
					
						new_user_input1_3 = -1
						while new_user_input1_3 != 0:
			
							addName = """

							Add Name
							0 >>> Back

								"""

							print(addName)
							new_user_input1_3 = int(input("your choice: "))
					
							match new_user_input1_3:
								
								case _: 
									if new_user_input1_3 != 0:  print("Invalid Input! Try Again..")
							
				
						#Add Name while loop ends
						


					case 4:	
						
						new_user_input1_4 = -1
						while new_user_input1_4 != 0:
		
							erase = """

							Erase
							0 >>> Back

								"""

							print(erase)
							new_user_input1_4 = int(input("your choice: "))
					
							match new_user_input1_4:
								
								case _: 
									if new_user_input1_4 != 0:  print("Invalid Input! Try Again..")
							
				
						#Erase while loop ends
						


					case 5: 	

						new_user_input1_5 = -1
						while new_user_input1_5 != 0:
		
							edit = """

							Edit
							0 >>> Back

								"""

							print(edit)
							new_user_input1_5 = int(input("your choice: "))
					
							match new_user_input1_5:
								
								case _: 
									if new_user_input1_5 != 0:  print("Invalid Input! Try Again..")
							
				
						#Edit while loop ends
						
		

					case 6:		
					
						new_user_input1_6 = -1
						while new_user_input1_6 != 0:
		
							assignTone = """

							Assign Tone
							0 >>> Back

								"""

							print(assignTone)
							new_user_input1_6 = int(input("your choice: "))
					
							match new_user_input1_6:
								
								case _: 
									if new_user_input1_6 != 0:  print("Invalid Input! Try Again..")
							
				
						#Assign Tone while loop ends
						


					case 7: 	
		
						new_user_input1_7 = -1
						while new_user_input1_7 != 0:
		 
							sendBcard = """

							Send B'card
							0 >>> Back

								"""

							print(sendBcard)
							new_user_input1_7 = int(input("your choice: "))
					
							match new_user_input1_7:
								
								case _: 
									if new_user_input1_7 != 0:  print("Invalid Input! Try Again..")
							
				
						#Send B'card while loop ends
						


					case 8: 	
		
						new_user_input1_8 = -1
						while new_user_input1_8 != 0:
		
							options = """

							Options
							Select a number
							1 >>> Type of View
							2 >>> Memory Status
							0 >>> Back

								"""

							print(options)
							new_user_input1_8 = int(input("your choice: "))
					
							match new_user_input1_8:
								case 1: 
									new_user_input1_8_1 = -1
									while new_user_input1_8_1 != 0:
		
										typeOfView = """

										Type of View
										0 >>> Back

											"""

										print(typeOfView)
										new_user_input1_8_1 = int(input("your choice: "))
					
										match new_user_input1_8_1:
											
											case _: 
												if new_user_input1_8_1 != 0:  print("Invalid Input! Try Again..")
										
				
									#Type of View while loop ends
									


								case 2: 
									new_user_input1_8_2 = -1
									while new_user_input1_8_2 != 0:
		
										memoryStatus = """

										Memory Status
										0 >>> Back

											"""

										print(memoryStatus)
										new_user_input1_8_2 = int(input("your choice: "))
					
										match new_user_input1_8_2:
										
											case _: 
												if new_user_input1_8_2 != 0:  print("Invalid Input! Try Again..")
										
				
									#Memory Status while loop ends
									

		
								case _: 
									if new_user_input1_8 != 0:  print("Invalid Input! Try Again..")

							
				
						#Options while loop end
						


					case 9: 	
		
						new_user_input1_9 = -1
						while new_user_input1_9 != 0:
		
							speedDials = """

							Speed Dials
							0 >>> Back

								"""

							print(speedDials)
							new_user_input1_9 = int(input("your choice: "))
					
							match new_user_input1_9:
								
								case _: 
									if new_user_input1_9 != 0:  print("Invalid Input! Try Again..")
							
				
						#Speed Dials while loop ends
						


					case 10: 	
		
						new_user_input1_10 = -1
						while new_user_input1_10 != 0:
		
							voiceTags = """

							Voice Tags
							0 >>> Back

								"""

							print(voiceTags)
							new_user_input1_10 = int(input("your choice: "))
					
							match new_user_input1_10:
							
								case _: 
									if new_user_input1_10 != 0:  print("Invalid Input! Try Again..")
							
				
						#Voice Tags while loop ends
						


					case _: 
						if new_user_input1 != 0:  print("Invalid Input! Try Again..")
					
				#match end for phonebook

			#Phonebook while loop ends

		
		case 2: 
			new_user_input2 = -1
			while new_user_input2 != 0:

				messages  = """

				Messages
				Select a number
				1 >>> Write Message
				2 >>> Indox
				3 >>> Outbox
				4 >>> Picture Message
				5 >>> Templates
				6 >>> Smileys
				7 >>> Message Settings
				8 >>> Info Service
				9 >>> Voice Mailbox Number
				10 >>> Service Command Editor
				0 >>> Back

					"""

				print(messages)
				new_user_input2 = int(input("your choice: "))

				match new_user_input2:


					case 1: 	
		
						new_user_input2_1 = -1
						while new_user_input2_1 != 0:
		
							writeMessage = """

							Write Message
							0 >>> Back

								"""

							print(writeMessage)
							new_user_input2_1 = int(input("your choice: "))
					
							match new_user_input2_1:
								
								case _: 
									if new_user_input2_1 != 0:  print("Invalid Input! Try Again..")
							
				
						#Write Message while loop ends
						


					case 2: 	

						new_user_input2_2 = -1
						while new_user_input2_2 != 0:
		
							inbox = """

							Inbox
							0 >>> Back

								"""

							print(inbox)
							new_user_input2_2 = int(input("your choice: "))
					
							match new_user_input2_2:
								
								case _: 
									if new_user_input2_2 != 0:  print("Invalid Input! Try Again..")
							
				
						#Inbox while loop ends
						

					
					case 3:		
					
						new_user_input2_3 = -1
						while new_user_input2_3 != 0:
			
							outbox = """

							Outbox
							0 >>> Back

								"""

							print(outbox)
							new_user_input2_3 = int(input("your choice: "))
					
							match new_user_input2_3:
								
								case _: 
									if new_user_input2_3 != 0:  print("Invalid Input! Try Again..")
							
				
						#Outbox while loop ends
						


					case 4:	
						
						new_user_input2_4 = -1
						while new_user_input2_4 != 0:
		
							pictureMessage = """

							Picture Message
							0 >>> Back

								"""

							print(pictureMessage)
							new_user_input2_4 = int(input("your choice: "))
					
							match new_user_input2_4:
								
								case _: 
									if new_user_input2_4 != 0:  print("Invalid Input! Try Again..")
							
				
						#Picture Message while loop ends
						


					case 5: 	

						new_user_input2_5 = -1
						while new_user_input2_5 != 0:
		
							templates = """

							Templates
							0 >>> Back

								"""

							print(templates)
							new_user_input2_5 = int(input("your choice: "))
					
							match new_user_input2_5:
								
								case _: 
									if new_user_input2_5 != 0:  print("Invalid Input! Try Again..")
							
				
						#Templates while loop ends
						
		

					case 6:		
					
						new_user_input2_6 = -1
						while new_user_input2_6 != 0:
		
							smileys = """

							Smileys
							0 >>> Back

								"""

							print(smileys)
							new_user_input2_6 = int(input("your choice: "))
					
							match new_user_input2_6:
								
								case _: 
									if new_user_input2_6 != 0:  print("Invalid Input! Try Again..")
							
				
						#Smileys while loop ends
						


					case 7:
						
						new_user_input2_7 = -1
						while new_user_input2_7 != 0:
		
							messageSettings = """

							Message Settings 
							Select a number
							1 >>> Set1
							2 >>> Common
							0 >>> Back

								"""

							print(messageSettings)
							new_user_input2_7 = int(input("your choice: "))
					
							match new_user_input2_7:
								case 1: 
									new_user_input2_7_1 = -1
									while new_user_input2_7_1 != 0:
		
										set1 = """

										Set1
										1 >>> Message Centre Number
										2 >>> Messages Sent As
										3 >>> Message Validity
										0 >>> Back

											"""

										print(set1)
										new_user_input2_7_1 = int(input("your choice: "))
					
										match new_user_input2_7_1:
											case 1:
												new_user_input2_7_1_1 = -1
												while new_user_input2_7_1_1 != 0:

													messageCentreNum ="""

													Message Centre Number
													0 >>> Back

														"""

													print(messageCentreNum)
													new_user_input2_7_1_1 = int(input("your choice: "))

													match new_user_input2_7_1_1:
														
														case _: 
															if new_user_input2_7_1_1 != 0:  print("Invalid Input! Try Again..")
																                                     

												
												

											case 2:  
												new_user_input2_7_1_2 = -1
												while new_user_input2_7_1_2 != 0:

													messageSentAs ="""

													Message Sent As
													0 >>> Back

														"""

													print(messageSentAs)
													new_user_input2_7_1_2 = int(input("your choice: "))

													match new_user_input2_7_1_2:
														
														case _: 
															if new_user_input2_7_1_2 != 0:  print("Invalid Input! Try Again..")
																                                     

												
												

											case 3:
												new_user_input2_7_1_3 = -1
												while new_user_input2_7_1_3 != 0:

													messageValidity ="""

													Message Validity
													0 >>> Back

														"""

													print(messageValidity)
													new_user_input2_7_1_3 = int(input("your choice: "))

													match new_user_input2_7_1_3:
														
														case _: 
															if new_user_input2_7_1_3 != 0:  print("Invalid Input! Try Again..")
																                                     

												
												


											case _: 
												if new_user_input2_7_1 != 0:  print("Invalid Input! Try Again..")

										
				
									#Set1 while loop ends
									


								case 2: 
									new_user_input2_7_2 = -1
									while new_user_input2_7_2 != 0:
		
										common = """

										Common
										1 >>> Delivery Reports
										2 >>> Reply Via Same Centre
										3 >>> Character Support
										0 >>> Back

											"""

										print(common)
										new_user_input2_7_2 = int(input("your choice: "))
					
										match new_user_input2_7_2:

											case 1:
												new_user_input2_7_2_1 = -1
												while new_user_input2_7_2_1 != 0:

													deliveryReports="""

													Delivery Reports
													0 >>> Back

														"""

													print(deliveryReports)
													new_user_input2_7_2_1 = int(input("your choice: "))

													match new_user_input2_7_2_1:
														
														case _: 
															if new_user_input2_7_2_1 != 0:  print("Invalid Input! Try Again..")
																                                     

												
												

											case 2:  
												new_user_input2_7_2_2 = -1
												while new_user_input2_7_2_2 != 0:

													reply ="""

													Reply Via Same Centre
													0 >>> Back

														"""

													print(reply)
													new_user_input2_7_2_2 = int(input("your choice: "))

													match new_user_input2_7_2_2:
														
														case _: 
															if new_user_input2_7_2_2 != 0:  print("Invalid Input! Try Again..")
																                                     

												
												

											case 3:
												new_user_input2_7_2_3 = -1
												while new_user_input2_7_2_3 != 0:

													characterSupport ="""

													Character Support
													0 >>> Back

														"""

													print(characterSupport)
													new_user_input2_7_2_3 = int(input("your choice: "))

													match new_user_input2_7_2_3:
														
														case _: 
															if new_user_input2_7_2_3 != 0:  print("Invalid Input! Try Again..")
																                                     

												
												


											case _: 
												if new_user_input2_7_2 != 0:  print("Invalid Input! Try Again..")

										

										
				
									#Common while loop ends
									

		
								case _: 
									if new_user_input2_7 != 0:  print("Invalid Input! Try Again..")

							
				
						#Message Settings while loop end
						




					case 8: 	
		
						new_user_input2_8 = -1
						while new_user_input2_8 != 0:
		
							infoService = """

							Info Service
							0 >>> Back

								"""

							print(infoService)
							new_user_input2_8 = int(input("your choice: "))
					
							match new_user_input2_8:
								
								case _: 
									if new_user_input2_8 != 0:  print("Invalid Input! Try Again..")
							
				
						#Info Service while loop ends
						


					case 9: 	

						new_user_input2_9 = -1
						while new_user_input2_9 != 0:
		
							voiceMailboxNumber = """

							Voice Mailbox Number 
							0 >>> Back

								"""

							print(voiceMailboxNumber)
							new_user_input2_9 = int(input("your choice: "))
					
							match new_user_input2_9:
								
								case _: 
									if new_user_input2_9 != 0:  print("Invalid Input! Try Again..")
							
				
						#Voice Mailbox Number while loop ends
						

					
					case 10:		
					
						new_user_input2_10 = -1
						while new_user_input2_10 != 0:
			
							serviceCommandEditor = """

							Service Command Editor 
							0 >>> Back

								"""

							print(serviceCommandEditor)
							new_user_input2_10 = int(input("your choice: "))
					
							match new_user_input2_10:
								
								case _: 
									if new_user_input2_10 != 0:  print("Invalid Input! Try Again..")
							
				
						#Service Command Editor while loop ends
						


					case _: 
						if new_user_input2 != 0:  print("Invalid Input! Try Again..")

			#messages while loop end		

		case 3: 	
		
			new_user_input3 = -1
			while new_user_input3 != 0:
		
				chat = """

				Chat
				0 >>> Back

					"""

				print(chat)
				new_user_input3 = int(input("your choice: "))
					
				match new_user_input3:
					
					case _: 
						if new_user_input3 != 0:  print("Invalid Input! Try Again..")
				
				
			#Chat while loop ends

		case 4: 		

			new_user_input4 = -1
			while new_user_input4 != 0:

				callRegister = """

				Call Register
				Select a number
				1 >>> Missed Calls
				2 >>> Recieved Calls
				3 >>> Dialled Numbers
				4 >>> Erase Recent Call Lists
				5 >>> Show Call Duration
				6 >>> Show Call Costs
				7 >>> Call Cost Settings
				8 >>> Prepaid Credit
				0 >>> Back

						"""
				
				print(callRegister)
				new_user_input4 = int(input("your choice: "))
					
				match new_user_input4:
					case 1: 	
		
						new_user_input4_1 = -1
						while new_user_input4_1 != 0:
		
							missedCalls = """

							Missed Calls
							0 >>> Back

								"""

							print(missedCalls)
							new_user_input4_1 = int(input("your choice: "))
					
							match new_user_input4_1:
								
								case _: 
									if new_user_input4_1 != 0:  print("Invalid Input! Try Again..")
							
				
						#Missed Calls while loop ends
						


					case 2: 	

						new_user_input4_2 = -1
						while new_user_input4_2 != 0:
		
							recievedCalls = """

							Recieved Calls
							0 >>> Back

								"""

							print(recievedCalls)
							new_user_input4_2 = int(input("your choice: "))
					
							match new_user_input4_2:
								
								case _: 
									if new_user_input4_2 != 0:  print("Invalid Input! Try Again..")
							
				
						#Recieved Calls while loop ends
						

					
					case 3:		
					
						new_user_input4_3 = -1
						while new_user_input4_3 != 0:
			
							dialledNumbers = """

							Dialled Numbers
							0 >>> Back

								"""

							print(dialledNumbers)
							new_user_input4_3 = int(input("your choice: "))
					
							match new_user_input4_3:
								
								case _: 
									if new_user_input4_3 != 0:  print("Invalid Input! Try Again..")
							
				
						#Dialled Numbers while loop ends
						


					case 4:	
						
						new_user_input4_4 = -1
						while new_user_input4_4 != 0:
		
							eraseRecentCallLists = """

							Erase Recent Call Lists
							0 >>> Back

								"""

							print(eraseRecentCallLists)
							new_user_input4_4 = int(input("your choice: "))
					
							match new_user_input4_4:
								
								case _: 
									if new_user_input4_4 != 0:  print("Invalid Input! Try Again..")
							
				
						#Erase Recent Call Lists while loop ends
						


					case 5: 	

						new_user_input4_5 = -1
						while new_user_input4_5 != 0:
		
							showCallDuration = """

							Show Call Duration
							1 >>> Last Call Duration
							2 >>> All Calls' Duration
							3 >>> Recieved Call Duration
							4 >>> Dialled Calls Duration
							5 >>> Clear Times
							0 >>> Back

								"""

							print(showCallDuration)
							new_user_input4_5 = int(input("your choice: "))
					
							match new_user_input4_5:
								case 1:
									new_user_input4_5_1 = -1
									while new_user_input4_5_1 != 0:
		
										lastCallDuration = """

										Last Call Duration
										0 >>> Back

											"""

										print(lastCallDuration)
										new_user_input4_5_1 = int(input("your choice: "))
					
										match new_user_input4_5_1:
											
											case _: 
												if new_user_input4_5_1 != 0:  print("Invalid Input! Try Again..")
										
				
									#Last Call Duration while loop ends
									


								case 2: 
									new_user_input4_5_2 = -1
									while new_user_input4_5_2 != 0:
		
										allCallsDuration = """

										All Calls' Duration
										0 >>> Back

											"""

										print(allCallsDuration)
										new_user_input4_5_2 = int(input("your choice: "))
					
										match new_user_input4_5_2:
											
											case _: 
												if new_user_input4_5_2 != 0:  print("Invalid Input! Try Again..")
										
				
									#All Calls' Duration while loop ends
									


								case 3: 
									new_user_input4_5_3 = -1
									while new_user_input4_5_3 != 0:
		
										recievedCallsDuration = """

										Recieved Calls' Duration
										0 >>> Back

											"""

										print(recievedCallsDuration)
										new_user_input4_5_3 = int(input("your choice: "))
					
										match new_user_input4_5_3:
											
											case _: 
												if new_user_input4_5_3 != 0:  print("Invalid Input! Try Again..")
										
				
									#Recieved Calls' Duration while loop ends
									


								case 4: 
									new_user_input4_5_4 = -1
									while new_user_input4_5_4 != 0:
		
										dialledCallsDuration = """

										Dialled Calls' Duration
										0 >>> Back

											"""

										print(dialledCallsDuration )
										new_user_input4_5_4 = int(input("your choice: "))
					
										match new_user_input4_5_4:
											
											case _: 
												if new_user_input4_5_4 != 0:  print("Invalid Input! Try Again..")
										
				
									#Dailled Calls' Duration while loop ends
									


								case 5: 
									new_user_input4_5_5 = -1
									while new_user_input4_5_5 != 0:
		
										clearTimes = """

										Clear Times
										0 >>> Back

											"""

										print(clearTimes )
										new_user_input4_5_5 = int(input("your choice: "))
					
										match new_user_input4_5_5:
											
											case _: 
												if new_user_input4_5_5 != 0:  print("Invalid Input! Try Again..")
										
				
									#Clear Times while loop ends
									


								case _: 
									if new_user_input4_5 != 0:  print("Invalid Input! Try Again..")

							
				
						#Show Call Duration while loop end
						
		

					case 6:		
					
						new_user_input4_6 = -1
						while new_user_input4_6 != 0:
		
							showCallCosts= """

							Show Call Costs
							1 >>> Last Call Cost
							2 >>> All Calls' Cost
							3 >>> Clear Counters
							0 >>> Back

								"""

							print(showCallCosts)
							new_user_input4_6 = int(input("your choice: "))
					
							match new_user_input4_6:
								case 1:
									new_user_input4_6_1 = -1
									while new_user_input4_6_1 != 0:
		
										lastCallCost = """

										Last Call Cost
										0 >>> Back

											"""

										print(lastCallCost)
										new_user_input4_6_1 = int(input("your choice: "))
					
										match new_user_input4_6_1:
											
											case _: 
												if new_user_input4_6_1 != 0:  print("Invalid Input! Try Again..")
										
				
									#Last Call Cost while loop ends
									


								case 2: 
									new_user_input4_6_2 = -1
									while new_user_input4_6_2 != 0:
		
										allCallsCost = """

										All Calls' Cost
										0 >>> Back

											"""

										print(allCallsCost)
										new_user_input4_6_2 = int(input("your choice: "))
					
										match new_user_input4_6_2:
											
											case _: 
												if new_user_input4_6_2 != 0:  print("Invalid Input! Try Again..")
										
				
									#All Calls' Cost while loop ends
									


								case 3: 
									new_user_input4_6_3 = -1
									while new_user_input4_6_3 != 0:
		
										clearCounters = """

										Clear Counters
										0 >>> Back

											"""

										print(clearCounters)
										new_user_input4_6_3 = int(input("your choice: "))
					
										match new_user_input4_6_3:
											case _: 
												if new_user_input4_6_3 != 0:  print("Invalid Input! Try Again..")
										
				
									#Clear Counters while loop ends
									

		
								case _: 
									if new_user_input4_6 != 0:  print("Invalid Input! Try Again..")

							


				
						#Show Call Costs while loop end
						


					case 7: 	
		
						new_user_input4_7 = -1
						while new_user_input4_7 != 0:
		
							callCostSettings = """
							
							Call Cost Settings
							Select a number
							1 >>> Call Cost Limit
							2 >>> Show Costs in
							0 >>> Back

								"""

							print(callCostSettings)
							new_user_input4_7 = int(input("your choice: "))
					
							match new_user_input4_7:
								case 1: 
									new_user_input4_7_1 = -1
									while new_user_input4_7_1 != 0:
		
										callCostLimit = """

										Call Cost Limit
										0 >>> Back

											"""

										print(callCostLimit)
										new_user_input4_7_1 = int(input("your choice: "))
					
										match new_user_input4_7_1:
											case _: 
												if new_user_input4_7_1 != 0:  print("Invalid Input! Try Again..")
										
				
									#Call Cost Limit while loop ends
									


								case 2: 
									new_user_input4_7_2 = -1
									while new_user_input4_7_2 != 0:
		
										showCostIn = """

										Show Cost in 
										0 >>> Back

											"""

										print(showCostIn)
										new_user_input4_7_2 = int(input("your choice: "))
					
										match new_user_input4_7_2:
											case _: 
												if new_user_input4_7_2 != 0:  print("Invalid Input! Try Again..")
										
				
									#Show Cost in  while loop ends
									

		
								case _: 
									if new_user_input4_7 != 0:  print("Invalid Input! Try Again..")

							
				
						#Call Cost Settings while loop end
						


					case 8: 	
		
						new_user_input4_8 = -1
						while new_user_input4_8 != 0:
		
							prepaidCredit = """

							Prepaid Credit
							0 >>> Back

								"""

							print(prepaidCredit)
							new_user_input4_8 = int(input("your choice: "))
					
							match new_user_input4_8:
								
								case _: 
									if new_user_input4_8 != 0:  print("Invalid Input! Try Again..")
							
				
						#Prepaid Credit while loop ends
						


					case _: 
						if new_user_input4 != 0:  print("Invalid Input! Try Again..")
					
				#match end for call register

			#Call Register while loop ends


		case 5: 	

			new_user_input5 = -1
			while new_user_input5 != 0:

				Tones = """
				Tones
				Select a number
				1 >>> Ringing Tone
				2 >>> Ringing Volume
				3 >>> Incoming Call Alert
				4 >>> Composer
				5 >>> Message Alert Tone
				6 >>> Key Tones
				7 >>> Warning and Game Tones
				8 >>> Vibrating Alert
				9 >>> Screen Saver
				0 >>> Back

						"""

				print(Tones)
				new_user_input5 = int(input("your choice: "))

				match new_user_input5:
					case 1: 	
		
						new_user_input5_1 = -1
						while new_user_input5_1 != 0:
		
							ringingTone = """

							Ringing Tone
							0 >>> Back

								"""

							print(ringingTone)
							new_user_input5_1 = int(input("your choice: "))
					
							match new_user_input5_1:
								
								case _: 
									if new_user_input5_1 != 0:  print("Invalid Input! Try Again..")
							
				
						#Ringing Tone while loop ends
						


					case 2: 	

						new_user_input5_2 = -1
						while new_user_input5_2 != 0:
		
							ringingVolume = """

							Ringing Volume
							0 >>> Back

								"""

							print(ringingVolume)
							new_user_input5_2 = int(input("your choice: "))
					
							match new_user_input5_2:
								
								case _: 
									if new_user_input5_2 != 0:  print("Invalid Input! Try Again..")
							
				
						#Ringing Volume Nos while loop ends
						

					
					case 3:		
					
						new_user_input5_3 = -1
						while new_user_input5_3 != 0:
			
							incomingCall = """

							Incoming Call Alert
							0 >>> Back

								"""

							print(incomingCall)
							new_user_input5_3 = int(input("your choice: "))
					
							match new_user_input5_3:
								
								case _: 
									if new_user_input5_3 != 0:  print("Invalid Input! Try Again..")
							
				
						#Incoming Call Alert  while loop ends
						


					case 4:	
						
						new_user_input5_4 = -1
						while new_user_input5_4 != 0:
		
							composer = """

							Composer
							0 >>> Back

								"""

							print(composer)
							new_user_input5_4 = int(input("your choice: "))
					
							match new_user_input5_4:
								
								case _: 
									if new_user_input5_4 != 0:  print("Invalid Input! Try Again..")
							
				
						#Composer while loop ends
						


					case 5: 	

						new_user_input5_5 = -1
						while new_user_input5_5 != 0:
		
							messageAlert = """

							Message Alert Tone
							0 >>> Back

								"""

							print(messageAlert)
							new_user_input5_5 = int(input("your choice: "))
					
							match new_user_input5_5:
								
								case _: 
									if new_user_input5_5 != 0:  print("Invalid Input! Try Again..")
							
				
						#Message Alert Tone while loop ends
						
		

					case 6:		
					
						new_user_input5_6 = -1
						while new_user_input5_6 != 0:
		
							keyTones = """

							Key Tones
							0 >>> Back

								"""

							print(keyTones)
							new_user_input5_6 = int(input("your choice: "))
					
							match new_user_input5_6:
								
								case _: 
									if new_user_input5_6 != 0:  print("Invalid Input! Try Again..")
							
				
						#Key Tones while loop ends
						


					case 7: 	
		
						new_user_input5_7 = -1
						while new_user_input5_7 != 0:
		
							warning = """

							Warning and Game Tones 
							0 >>> Back

								"""

							print(warning)
							new_user_input5_7 = int(input("your choice: "))
					
							match new_user_input5_7:
								
								case _: 
									if new_user_input5_7 != 0:  print("Invalid Input! Try Again..")
							
				
						#Warning and Game Tones while loop ends
						


					case 8: 	
		
						new_user_input5_8 = -1
						while new_user_input5_8 != 0:
		
							vibratingAlert = """

							Vibrating Alert
							0 >>> Back

								"""

							print(vibratingAlert)
							new_user_input5_8 = int(input("your choice: "))
					
							match new_user_input5_8:
								
								case _: 
									if new_user_input5_8 != 0:  print("Invalid Input! Try Again..")

							
				
						#Vibrating Alert while loop end
						


					case 9: 	
		
						new_user_input5_9 = -1
						while new_user_input5_9 != 0:
		
							screenSaver = """

							Screen Saver
							0 >>> Back

								"""

							print(screenSaver)
							new_user_input5_9 = int(input("your choice: "))
					
							match new_user_input5_9:
								
								case _: 
									if new_user_input5_9 != 0:  print("Invalid Input! Try Again..")
							
				
						#Screen Saver while loop ends
						


					case _: 
						if new_user_input5 != 0:  print("Invalid Input! Try Again..")
					
				#match end for Tones

			#Tones while loop ends


		case 6: 

			new_user_input6 = -1
			while new_user_input6 != 0:

				settings = """

				Settings
				Select a number
				1 >>> Call Settings
				2 >>> Phone Settings
				3 >>> Security Settings
				4 >>> Restore Factory Settings
				0 >>> Back

					"""
				
				print(settings)
				new_user_input6 = int(input("your choice: "))
					
				match new_user_input6:  
					case 1: 
		
						new_user_input6_1 = -1
						while new_user_input6_1 != 0:
							callSettings= """

							Call Settings
							Select a number
							1 >>> Automatic Redial
							2 >>> Speed Dialling
							3 >>> Call Waiting Options
							4 >>> Own Number Sending
							5 >>> Phone Line in Use
							6 >>> Automatic Answer
							0 >>> Back

									"""

							print(callSettings)
							new_user_input6_1 = int(input("your choice: "))
				
							match new_user_input6_1:  
								case 1: 
									new_user_input6_1_1 = -1
									while new_user_input6_1_1 != 0:
		
										automaticRedial = """

										Automatic Redial
										0 >>> Back

											"""

										print(automaticRedial)
										new_user_input6_1_1 = int(input("your choice: "))
					
										match new_user_input6_1_1:
											
											case _: 
												if new_user_input6_1_1 != 0:  print("Invalid Input! Try Again..")
										
				
									#Automatic Redial while loop ends
									


								case 2: 
									new_user_input6_1_2 = -1
									while new_user_input6_1_2 != 0:
		
										speedDialling = """

										Speed Dialling
										0 >>> Back

											"""

										print(speedDialling)
										new_user_input6_1_2 = int(input("your choice: "))
					
										match new_user_input6_1_2:
											
											case _: 
												if new_user_input6_1_2 != 0:  print("Invalid Input! Try Again..")
										
				
									#Speed Dialling while loop ends
									



								case 3: 
									new_user_input6_1_3 = -1
									while new_user_input6_1_3 != 0:
		
										callWaiting = """

										Call Waiting Options
										0 >>> Back

											"""

										print(callWaiting)
										new_user_input6_1_3 = int(input("your choice: "))
					
										match new_user_input6_1_3:
											
											case _: 
												if new_user_input6_1_3 != 0:  print("Invalid Input! Try Again..")
										
				
									#Call Waiting Options while loop ends
									



								case 4: 
									new_user_input6_1_4 = -1
									while new_user_input6_1_4 != 0:
		
										ownNumber = """

										Own Number Sending 
										0 >>> Back

											"""

										print(ownNumber)
										new_user_input6_1_4 = int(input("your choice: "))
					
										match new_user_input6_1_4:
											
											case _: 
												if new_user_input6_1_4 != 0:  print("Invalid Input! Try Again..")
										
				
									#Own Number Sending while loop ends
									



								case 5: 
									new_user_input6_1_5 = -1
									while new_user_input6_1_5 != 0:
		
										phoneLine = """

										Phone Line in Use
										0 >>> Back

											"""

										print(phoneLine)
										new_user_input6_1_5 = int(input("your choice: "))
					
										match new_user_input6_1_5:
											
											case _: 
												if new_user_input6_1_5 != 0:  print("Invalid Input! Try Again..")
										
				
									#Phone Line in Use while loop ends
									


								case 6: 
									new_user_input6_1_6 = -1
									while new_user_input6_1_6 != 0:
		
										autoAnswer = """

										Automatic Answer 
										0 >>> Back

											"""

										print(autoAnswer )
										new_user_input6_1_6 = int(input("your choice: "))
					
										match new_user_input6_1_6:
											
											case _: 
												if new_user_input6_1_6 != 0:  print("Invalid Input! Try Again..")
										
				
									#Automatic Answer while loop ends
									
		
								case _: 
									if new_user_input6_1 != 0:  print("Invalid Input! Try Again..")


							#end match for call settings
							
						
						

					case 2: 
				
						new_user_input6_2 = -1
						while new_user_input6_2 != 0:

							phoneSettings= """

							Phone Settings
							Select a number
							1 >>> Language
							2 >>> Cell Info Display
							3 >>> Welcome Note
							4 >>> Network Selection
							5 >>> Lights
							6 >>> Confirm SIM Service Actions
							0 >>> Back

									"""

							print(phoneSettings)
							new_user_input6_2 = int(input("your choice: "))
				
							match new_user_input6_2:


								case 1: 
									new_user_input6_2_1 = -1
									while new_user_input6_2_1 != 0:
		
										language = """

										Language
										0 >>> Back

											"""

										print(language)
										new_user_input6_2_1 = int(input("your choice: "))
					
										match new_user_input6_2_1:
											
											case _: 
												if new_user_input6_2_1 != 0:  print("Invalid Input! Try Again..")
										
				
									#Language while loop ends
									


								case 2: 
									new_user_input6_2_2 = -1
									while new_user_input6_2_2 != 0:
		
										callInfoDisplay = """

										Call Info Display
										0 >>> Back

											"""

										print(callInfoDisplay)
										new_user_input6_2_2 = int(input("your choice: "))
					
										match new_user_input6_2_2:
											
											case _: 
												if new_user_input6_2_2 != 0:  print("Invalid Input! Try Again..")
										
				
									#Call Info Display while loop ends
									



								case 3: 
									new_user_input6_2_3 = -1
									while new_user_input6_2_3 != 0:
		
										welcomeNotes = """

										Welcome Note
										0 >>> Back

											"""

										print(welcomeNotes)
										new_user_input6_2_3 = int(input("your choice: "))
					
										match new_user_input6_2_3:
											
											case _: 
												if new_user_input6_2_3 != 0:  print("Invalid Input! Try Again..")
										
				
									#welcome Notes  while loop ends
									



								case 4: 
									new_user_input6_2_4 = -1
									while new_user_input6_2_4 != 0:
		
										networkSelection = """
										Network Selection
										0 >>> Back

											"""

										print(networkSelection)
										new_user_input6_2_4 = int(input("your choice: "))
					
										match new_user_input6_2_4:
											
											case _: 
												if new_user_input6_2_4 != 0:  print("Invalid Input! Try Again..")
										
				
									#Network Selection while loop ends
									


								case 5: 
									new_user_input6_2_5 = -1
									while new_user_input6_2_5 != 0:
		
										lights = """

										Lights
										0 >>> Back

											"""

										print(lights)
										new_user_input6_2_5 = int(input("your choice: "))
					
										match new_user_input6_2_5:
											
											case _: 
												if new_user_input6_2_5 != 0:  print("Invalid Input! Try Again..")
										
				
									#Lights while loop ends
									


								case 6: 
									new_user_input6_2_6 = -1
									while new_user_input6_2_6 != 0:
		
										simServiceAction = """

										Confirm SIM Service Actions
										0 >>> Back

											"""

										print(simServiceAction)
										new_user_input6_2_6 = int(input("your choice: "))
					
										match new_user_input6_2_6:
											
											case _: 
												if new_user_input6_2_6 != 0:  print("Invalid Input! Try Again..")
										
				
									#Confirm SIM Service Actions while loop ends
									


		
								case _: 
									if new_user_input6_2 != 0:  print("Invalid Input! Try Again..")


							#end match for phone settings
				
						
						

					case 3:

						new_user_input6_3 = -1
						while new_user_input6_3 != 0:


							securitySettings= """

							Security Settings
							Select a number
							1 >>> Pin Code Request
							2 >>> Call Barring Service
							3 >>> Fixed Dialling
							4 >>> Closed User Group
							5 >>> Phone Security
							6 >>> Change Access Codes
							0 >>> Back

									"""

							print(securitySettings)
							new_user_input6_3 = int(input("your choice: "))
				
							match new_user_input6_3:


								case 1: 
									new_user_input6_3_1 = -1
									while new_user_input6_3_1 != 0:
		
										pinCodeRequest = """

										Pin Code Request
										0 >>> Back

											"""

										print(pinCodeRequest)
										new_user_input6_3_1 = int(input("your choice: "))
					
										match new_user_input6_3_1:
											
											case _: 
												if new_user_input6_3_1 != 0:  print("Invalid Input! Try Again..")
										
				
									#Pin Code Request while loop ends
									


								case 2: 
									new_user_input6_3_2 = -1
									while new_user_input6_3_2 != 0:
		
										callBarringService = """

										Call Barring Service
										0 >>> Back

											"""

										print(callBarringService)
										new_user_input6_3_2 = int(input("your choice: "))
					
										match new_user_input6_3_2:
											
											case _: 
												if new_user_input6_3_2 != 0:  print("Invalid Input! Try Again..")
										
				
									#Call Barring Service while loop ends
									


								case 3: 
									new_user_input6_3_3 = -1
									while new_user_input6_3_3 != 0:
		
										fixedDialling = """

										Fixed Dialling 
										0 >>> Back

											"""

										print(fixedDialling)
										new_user_input6_3_3 = int(input("your choice: "))
					
										match new_user_input6_3_3:
											
											case _: 
												if new_user_input6_3_3 != 0:  print("Invalid Input! Try Again..")
										
				
									#Fixed Dialling Notes  while loop ends
									



								case 4: 
									new_user_input6_3_4 = -1
									while new_user_input6_3_4 != 0:
		
										closedUserGroup = """
										Closed User Group
										0 >>> Back

											"""

										print(closedUserGroup)
										new_user_input6_3_4 = int(input("your choice: "))
					
										match new_user_input6_3_4:
											
											case _: 
												if new_user_input6_3_4 != 0:  print("Invalid Input! Try Again..")
										
				
									#Closed User Group while loop ends
									



								case 5: 
									new_user_input6_3_5 = -1
									while new_user_input6_3_5 != 0:
		
										phoneSecurity  = """

										Phone Security
										0 >>> Back

											"""

										print(phoneSecurity)
										new_user_input6_3_5 = int(input("your choice: "))
					
										match new_user_input6_3_5:
											
											case _: 
												if new_user_input6_3_5 != 0:  print("Invalid Input! Try Again..")
										
				
									#Phone Security while loop ends
									


								case 6: 
									new_user_input6_3_6 = -1
									while new_user_input6_3_6 != 0:
		
										changeAccessCodes = """

										Change Access Codes
										0 >>> Back

											"""

										print(changeAccessCodes)
										new_user_input6_3_6 = int(input("your choice: "))
					
										match new_user_input6_3_6:
											
											case _: 
												if new_user_input6_3_6 != 0:  print("Invalid Input! Try Again..")
										
				
									#Change Access Codes while loop ends
									
		
								case _: 
									if new_user_input6_3 != 0:  print("Invalid Input! Try Again..")

							#end match for Security Settings
							
						
						


					case 4:	

						new_user_input6_4 = -1
						while new_user_input6_4 != 0:
		
							factorySettings = """
					
							Restore Factory Settings
							0 >>> Back

								"""

							print(factorySettings)
							new_user_input6_4 = int(input("your choice: "))

							match new_user_input6_4:
								
								case _: 
									if new_user_input6_4 != 0:  print("Invalid Input! Try Again..")

							
						

					case _:
						if new_user_input6 != 0:  print("Invalid Input! Try Again..")


			#Settings while loop end
			

		case 7: 	

			new_user_input7 = -1
			while new_user_input7 != 0:
		
				callDivert = """

				Call Divert
				0 >>> Back

					"""

				print(callDivert)
				new_user_input7 = int(input("your choice: "))
					
				match new_user_input7:
					
					case _: 
						if new_user_input7 != 0:  print("Invalid Input! Try Again..")
				
				
			#Call Divert while loop ends

		
		case 8:

			new_user_input8 = -1
			while new_user_input8 != 0:
		
				games = """
				
				Games
				1. Rock, Paper, Scissors
				0 >>> Back

					"""

				print(games)
				new_user_input8 = int(input("your choice: "))
					
				match new_user_input8:

					case 1: 

						new_user_input8_1 = -1
						while new_user_input8_1 != 0:

							

							userWinCounter = 0
							compWinCounter = 0
							
							while userWinCounter != compWinCounter + 3 and userWinCounter + 3 != compWinCounter:
								print("\nChoose Scissors(0), Rock(1) or Paper(2: ")
								answer = int(input("your choice: "))
								compNum = random.randrange(3)
							
								if compNum == 0: 
									print("The Computer Chooses Scissors, ", end = "")
								elif compNum == 1:
									print("The Computer Chooses Rock, ", end = "")
								else: 
									print("The Computer Chooses Paper, ", end = "")
							
							
								if answer == 0:
									print("You Choose Scissors, ", end = "")
								elif answer == 1:
									print("You Choose Rock, ", end = "")
								elif answer == 2:
									print("You Choose Paper, ", end = "")
								else:
									print("Invalid c`mon! just 0s, 1s and 2s mate")
							
							
								if compNum == answer:
									print("It`s a Draw!")
								elif compNum == 0 and answer == 1:
									print("You Win!")
									userWinCounter += 1
								elif compNum == 1 and answer == 0:
									print("The Computer Wins!")
									compWinCounter += 1
								elif compNum == 1 and answer == 2:
									print("You Win!")
									userWinCounter += 1
								elif compNum == 2 and answer == 1:
									print("The Computer Wins!")
									compWinCounter += 1
								elif compNum == 2 and answer == 0:
									print("You Win!")
									userWinCounter += 1
								elif compNum == 0 and answer == 2:
									print("The Computer Wins!")
									compWinCounter += 1
									
							
							if userWinCounter == compWinCounter + 3:
								print("Game Over! You Won")
													
							if userWinCounter + 3 == compWinCounter:
								print("Game Over! The Computer Won")
		
							print()
							print("press 1 to continue. 0 to quit")
							new_user_input8_1 = int(input("your choice: "))
					
							match new_user_input8_1:

								case 0:
									new_user_input8_1 = 0
												

								case 1: continue

								case _: print("Invalid Input! Try Again..")

							
							continue

						#R.P.S game while loop ends
						
		
					case _: 
						if new_user_input8 != 0:  print("Invalid Input! Try Again..")
	


		case 9: 	
			
			new_user_input9 = -1
			while new_user_input9 != 0:
		
				calculator = """

				Calculator
				0 >>> Back

					"""

				print(calculator)
				new_user_input9 = int(input("your choice: "))
					
				match new_user_input9:
					
					case _: 
						if new_user_input9 != 0:  print("Invalid Input! Try Again..")
				
				
			#Calculator while loop ends
			

		
		case 10: 	
			
			new_user_input10 = -1
			while new_user_input10 != 0:
		
				reminders = """

				Reminders
				0 >>> Back

					"""

				print(reminders)
				new_user_input10 = int(input("your choice: "))
					
				match new_user_input10:
					
					case _: 
						if new_user_input10 != 0:  print("Invalid Input! Try Again..")
				
				
			#Reminders while loop ends
			


		case 11:		

			new_user_input11 = 1
			while new_user_input11 != 0:

				clock = """

				Clock
				Select a number
				1 >>> Alarm Clock
				2 >>> Clock Settings
				3 >>> Date Settings
				4 >>> Stopwatch
				5 >>> Countdown Timer
				6 >>> Auto Update Date and Time
				0 >>> Back

						"""

				print(clock)
				new_user_input11 = int(input("your choice: "))

				match new_user_input11:
		
					case 1: 	
		
						new_user_input11_1 = -1
						while new_user_input11_1 != 0:
		
							alarmClock = """

							Alarm Clock
							0 >>> Back

								"""

							print(alarmClock)
							new_user_input11_1 = int(input("your choice: "))
					
							match new_user_input11_1:
								
								case _: 
									if new_user_input11_1 != 0:  print("Invalid Input! Try Again..")
							
				
						
						


					case 2: 	

						new_user_input11_2 = -1
						while new_user_input11_2 != 0:
		
							clockSettings = """

							Clock Settings
							0 >>> Back

								"""

							print(clockSettings)
							new_user_input11_2 = int(input("your choice: "))
					
							match new_user_input11_2:
								
								case _: 
									if new_user_input11_2 != 0:  print("Invalid Input! Try Again..")
							
				
						
						

					
					case 3:		
					
						new_user_input11_3 = -1
						while new_user_input11_3 != 0:
			
							dateSettings = """

							Date Settings
							0 >>> Back

								"""

							print(dateSettings)
							new_user_input11_3 = int(input("your choice: "))
					
							match new_user_input11_3:
								
								case _: 
									if new_user_input11_3 != 0:  print("Invalid Input! Try Again..")
							
				
						
						


					case 4:	
						
						new_user_input11_4 = -1
						while new_user_input11_4 != 0:
		
							stopwatch = """

							Stopwatch
							0 >>> Back

								"""

							print(stopwatch)
							new_user_input11_4 = int(input("your choice: "))
					
							match new_user_input11_4:
								
								case _: 
									if new_user_input11_4 != 0:  print("Invalid Input! Try Again..")
							
				
						
						


					case 5: 	

						new_user_input11_5 = -1
						while new_user_input11_5 != 0:
		
							countdownTimer = """

							Countdown Timer
							0 >>> Back

								"""

							print(countdownTimer)
							new_user_input11_5 = int(input("your choice: "))
					
							match new_user_input11_5:
								
								case _: 
									if new_user_input11_5 != 0:  print("Invalid Input! Try Again..")
							
				
						
						
		

					case 6:		
					
						new_user_input11_6 = -1
						while new_user_input11_6 != 0:
		
							autoUpdate = """

							Auto Update Date and Time
							0 >>> Back

								"""

							print(autoUpdate)
							new_user_input11_6 = int(input("your choice: "))
					
							match new_user_input11_6:
								
								case _: 
									if new_user_input11_6 != 0:  print("Invalid Input! Try Again..")
							
				
						
						


					case _: 
						if new_user_input11 != 0:  print("Invalid Input! Try Again..")

					
				#match end for Clock

			#Clock while loop ends
		

		case 12: 	

			new_user_input12 = -1
			while new_user_input12 != 0:
		
				profiles = """

				Profiles
				0 >>> Back

					"""

				print(profiles)
				new_user_input12 = int(input("your choice: "))
					
				match new_user_input12:
					
					case _: 
						if new_user_input12 != 0:  print("Invalid Input! Try Again..")
				
				
			#Profiles while loop ends

		
		case 13: 	
			
			new_user_input13 = -1
			while new_user_input13 != 0:
		
				simServices = """

				SIM Services
				0 >>> Back

					"""

				print(simServices)
				new_user_input13 = int(input("your choice: "))
					
				match new_user_input13:
					
					case _: 
						if new_user_input13 != 0:  print("Invalid Input! Try Again..")
				
				
			#SIM Services while loop ends

		
		case _: 
			if user_input != 0:  print("Invalid Input! Try Again..")

	#match end for nokia menu

#nokia menu while loop end

print("Goodbye.")




