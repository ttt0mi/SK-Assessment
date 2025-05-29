import random
import menus
from menus import *


user_input = -1
while user_input != 0:
	
	print(phone_start())
	user_input = int(input("your choice: "))
	
	match user_input:

		case 1: 
			new_user_input1 = 1
			while new_user_input1 != 0:
				
				print(phonebook())
				new_user_input1 = int(input("your choice: "))

				match new_user_input1:
		
					case 1: 	
		
						new_user_input1_1 = -1
						while new_user_input1_1 != 0:

							print(search())
							new_user_input1_1 = int(input("your choice: "))
					
							match new_user_input1_1:
								
								case _: 
									if new_user_input1_1 != 0:  print("Invalid Input! Try Again..")

							
				
						#Search while loop ends
						


					case 2: 	

						new_user_input1_2 = -1
						while new_user_input1_2 != 0:

							print(services_nos())
							new_user_input1_2 = int(input("your choice: "))
					
							match new_user_input1_2:
								
								case _: 
									if new_user_input1_2 != 0:  print("Invalid Input! Try Again..")
							
				
						#Services Nos while loop ends
						

					
					case 3:		
					
						new_user_input1_3 = -1
						while new_user_input1_3 != 0:

							print(add_name())
							new_user_input1_3 = int(input("your choice: "))
					
							match new_user_input1_3:
								
								case _: 
									if new_user_input1_3 != 0:  print("Invalid Input! Try Again..")
							
						#Add Name while loop ends
						
					case 4:	
						
						new_user_input1_4 = -1
						while new_user_input1_4 != 0:

							print(erase())
							new_user_input1_4 = int(input("your choice: "))
					
							match new_user_input1_4:
								
								case _: 
									if new_user_input1_4 != 0:  print("Invalid Input! Try Again..")
							
						#Erase while loop ends

					case 5: 	

						new_user_input1_5 = -1
						while new_user_input1_5 != 0:

							print(edit())
							new_user_input1_5 = int(input("your choice: "))
					
							match new_user_input1_5:
								
								case _: 
									if new_user_input1_5 != 0:  print("Invalid Input! Try Again..")
							
				
						#Edit while loop ends
						
					case 6:		
					
						new_user_input1_6 = -1
						while new_user_input1_6 != 0:

							print(assign_tone())
							new_user_input1_6 = int(input("your choice: "))
					
							match new_user_input1_6:
								
								case _: 
									if new_user_input1_6 != 0:  print("Invalid Input! Try Again..")
							
				
						#Assign Tone while loop ends
					
					case 7: 	
		
						new_user_input1_7 = -1
						while new_user_input1_7 != 0:

							print(send_bcard())
							new_user_input1_7 = int(input("your choice: "))
					
							match new_user_input1_7:
								
								case _: 
									if new_user_input1_7 != 0:  print("Invalid Input! Try Again..")
							
				
						#Send B'card while loop ends
						


					case 8: 	
		
						new_user_input1_8 = -1
						while new_user_input1_8 != 0:

							print(options())
							new_user_input1_8 = int(input("your choice: "))
					
							match new_user_input1_8:
								case 1: 
									new_user_input1_8_1 = -1
									while new_user_input1_8_1 != 0:

										print(type_of_view())
										new_user_input1_8_1 = int(input("your choice: "))
					
										match new_user_input1_8_1:
											
											case _: 
												if new_user_input1_8_1 != 0:  print("Invalid Input! Try Again..")
										
				
									#Type of View while loop ends
									


								case 2: 
									new_user_input1_8_2 = -1
									while new_user_input1_8_2 != 0:

										print(memory_status())
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

							print(speed_dials())
							new_user_input1_9 = int(input("your choice: "))
					
							match new_user_input1_9:
								
								case _: 
									if new_user_input1_9 != 0:  print("Invalid Input! Try Again..")
							
				
						#Speed Dials while loop ends
						


					case 10: 	
		
						new_user_input1_10 = -1
						while new_user_input1_10 != 0:

							print(voice_tags())
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

				print(messages())
				new_user_input2 = int(input("your choice: "))

				match new_user_input2:


					case 1: 	
		
						new_user_input2_1 = -1
						while new_user_input2_1 != 0:

							print(write_message())
							new_user_input2_1 = int(input("your choice: "))
					
							match new_user_input2_1:
								
								case _: 
									if new_user_input2_1 != 0:  print("Invalid Input! Try Again..")
							
				
						#Write Message while loop ends
						


					case 2: 	

						new_user_input2_2 = -1
						while new_user_input2_2 != 0:
		
							print(inbox())
							new_user_input2_2 = int(input("your choice: "))
					
							match new_user_input2_2:
								
								case _: 
									if new_user_input2_2 != 0:  print("Invalid Input! Try Again..")
							
				
						#Inbox while loop ends
						

					
					case 3:		
					
						new_user_input2_3 = -1
						while new_user_input2_3 != 0:

							print(outbox())
							new_user_input2_3 = int(input("your choice: "))
					
							match new_user_input2_3:
								
								case _: 
									if new_user_input2_3 != 0:  print("Invalid Input! Try Again..")
							
				
						#Outbox while loop ends
						


					case 4:	
						
						new_user_input2_4 = -1
						while new_user_input2_4 != 0:

							print(picture_message())
							new_user_input2_4 = int(input("your choice: "))
					
							match new_user_input2_4:
								
								case _: 
									if new_user_input2_4 != 0:  print("Invalid Input! Try Again..")
							
				
						#Picture Message while loop ends
						


					case 5: 	

						new_user_input2_5 = -1
						while new_user_input2_5 != 0:

							print(templates())
							new_user_input2_5 = int(input("your choice: "))
					
							match new_user_input2_5:
								
								case _: 
									if new_user_input2_5 != 0:  print("Invalid Input! Try Again..")
							
				
						#Templates while loop ends
						
		

					case 6:		
					
						new_user_input2_6 = -1
						while new_user_input2_6 != 0:

							print(smileys())
							new_user_input2_6 = int(input("your choice: "))
					
							match new_user_input2_6:
								
								case _: 
									if new_user_input2_6 != 0:  print("Invalid Input! Try Again..")
							
				
						#Smileys while loop ends
						


					case 7:
						
						new_user_input2_7 = -1
						while new_user_input2_7 != 0:

							print(message_settings)
							new_user_input2_7 = int(input("your choice: "))
					
							match new_user_input2_7:
								case 1: 
									new_user_input2_7_1 = -1
									while new_user_input2_7_1 != 0:

										print(set1())
										new_user_input2_7_1 = int(input("your choice: "))
					
										match new_user_input2_7_1:
											case 1:
												new_user_input2_7_1_1 = -1
												while new_user_input2_7_1_1 != 0:

													print(message_centre_num())
													new_user_input2_7_1_1 = int(input("your choice: "))

													match new_user_input2_7_1_1:
														
														case _: 
															if new_user_input2_7_1_1 != 0:  print("Invalid Input! Try Again..")
																                                     

												
												

											case 2:  
												new_user_input2_7_1_2 = -1
												while new_user_input2_7_1_2 != 0:

													print(message_sent_as())
													new_user_input2_7_1_2 = int(input("your choice: "))

													match new_user_input2_7_1_2:
														
														case _: 
															if new_user_input2_7_1_2 != 0:  print("Invalid Input! Try Again..")
																                                     

												
												

											case 3:
												new_user_input2_7_1_3 = -1
												while new_user_input2_7_1_3 != 0:

													print(message_validity())
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

										print(common())
										new_user_input2_7_2 = int(input("your choice: "))
					
										match new_user_input2_7_2:

											case 1:
												new_user_input2_7_2_1 = -1
												while new_user_input2_7_2_1 != 0:

													print(delivery_reports())
													new_user_input2_7_2_1 = int(input("your choice: "))

													match new_user_input2_7_2_1:
														
														case _: 
															if new_user_input2_7_2_1 != 0:  print("Invalid Input! Try Again..")
																                                     

												
												

											case 2:  
												new_user_input2_7_2_2 = -1
												while new_user_input2_7_2_2 != 0:

													print(reply())
													new_user_input2_7_2_2 = int(input("your choice: "))

													match new_user_input2_7_2_2:
														
														case _: 
															if new_user_input2_7_2_2 != 0:  print("Invalid Input! Try Again..")
																                                     

												
												

											case 3:
												new_user_input2_7_2_3 = -1
												while new_user_input2_7_2_3 != 0:

													print(character_support())
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

							print(info_service())
							new_user_input2_8 = int(input("your choice: "))
					
							match new_user_input2_8:
								
								case _: 
									if new_user_input2_8 != 0:  print("Invalid Input! Try Again..")
							
				
						#Info Service while loop ends
						


					case 9: 	

						new_user_input2_9 = -1
						while new_user_input2_9 != 0:

							print(voice_mailbox_number())
							new_user_input2_9 = int(input("your choice: "))
					
							match new_user_input2_9:
								
								case _: 
									if new_user_input2_9 != 0:  print("Invalid Input! Try Again..")
							
				
						#Voice Mailbox Number while loop ends
						

					
					case 10:		
					
						new_user_input2_10 = -1
						while new_user_input2_10 != 0:

							print(service_command_editor())
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

				print(chat())
				new_user_input3 = int(input("your choice: "))
					
				match new_user_input3:
					
					case _: 
						if new_user_input3 != 0:  print("Invalid Input! Try Again..")
				
				
			#Chat while loop ends

		case 4: 		

			new_user_input4 = -1
			while new_user_input4 != 0:
				
				print(call_register())
				new_user_input4 = int(input("your choice: "))
					
				match new_user_input4:
					case 1: 	
		
						new_user_input4_1 = -1
						while new_user_input4_1 != 0:

							print(missed_calls())
							new_user_input4_1 = int(input("your choice: "))
					
							match new_user_input4_1:
								
								case _: 
									if new_user_input4_1 != 0:  print("Invalid Input! Try Again..")
							
				
						#Missed Calls while loop ends
						


					case 2: 	

						new_user_input4_2 = -1
						while new_user_input4_2 != 0:

							print(received_calls())  
							new_user_input4_2 = int(input("your choice: "))
					
							match new_user_input4_2:
								
								case _: 
									if new_user_input4_2 != 0:  print("Invalid Input! Try Again..")
							
				
						#Recieved Calls while loop ends
						

					
					case 3:		
					
						new_user_input4_3 = -1
						while new_user_input4_3 != 0:

							print(dialed_numbers())
							new_user_input4_3 = int(input("your choice: "))
					
							match new_user_input4_3:
								
								case _: 
									if new_user_input4_3 != 0:  print("Invalid Input! Try Again..")
							
				
						#Dialled Numbers while loop ends
						


					case 4:	
						
						new_user_input4_4 = -1
						while new_user_input4_4 != 0:

							print(erase_recent_call_lists())
							new_user_input4_4 = int(input("your choice: "))
					
							match new_user_input4_4:
								
								case _: 
									if new_user_input4_4 != 0:  print("Invalid Input! Try Again..")
							
				
						#Erase Recent Call Lists while loop ends
						


					case 5: 	

						new_user_input4_5 = -1
						while new_user_input4_5 != 0:

							print(show_call_duration())
							new_user_input4_5 = int(input("your choice: "))
					
							match new_user_input4_5:
								case 1:
									new_user_input4_5_1 = -1
									while new_user_input4_5_1 != 0:

										print(last_call_duration())
										new_user_input4_5_1 = int(input("your choice: "))
					
										match new_user_input4_5_1:
											
											case _: 
												if new_user_input4_5_1 != 0:  print("Invalid Input! Try Again..")
										
				
									#Last Call Duration while loop ends
									


								case 2: 
									new_user_input4_5_2 = -1
									while new_user_input4_5_2 != 0:

										print(all_calls_duration())
										new_user_input4_5_2 = int(input("your choice: "))
					
										match new_user_input4_5_2:
											
											case _: 
												if new_user_input4_5_2 != 0:  print("Invalid Input! Try Again..")
										
				
									#All Calls' Duration while loop ends
									


								case 3: 
									new_user_input4_5_3 = -1
									while new_user_input4_5_3 != 0:

										print(recieved_calls_duration())
										new_user_input4_5_3 = int(input("your choice: "))
					
										match new_user_input4_5_3:
											
											case _: 
												if new_user_input4_5_3 != 0:  print("Invalid Input! Try Again..")
										
				
									#Recieved Calls' Duration while loop ends
									


								case 4: 
									new_user_input4_5_4 = -1
									while new_user_input4_5_4 != 0:

										print(dialed_calls_duration())
										new_user_input4_5_4 = int(input("your choice: "))
					
										match new_user_input4_5_4:
											
											case _: 
												if new_user_input4_5_4 != 0:  print("Invalid Input! Try Again..")
										
				
									#Dialed Calls' Duration while loop ends
									


								case 5: 
									new_user_input4_5_5 = -1
									while new_user_input4_5_5 != 0:

										print(clear_times())
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

							print(show_call_costs())
							new_user_input4_6 = int(input("your choice: "))
					
							match new_user_input4_6:
								case 1:
									new_user_input4_6_1 = -1
									while new_user_input4_6_1 != 0:

										print(last_call_costs())
										new_user_input4_6_1 = int(input("your choice: "))
					
										match new_user_input4_6_1:
											
											case _: 
												if new_user_input4_6_1 != 0:  print("Invalid Input! Try Again..")
										
				
									#Last Call Cost while loop ends
									


								case 2: 
									new_user_input4_6_2 = -1
									while new_user_input4_6_2 != 0:

										print(all_calls_costs())
										new_user_input4_6_2 = int(input("your choice: "))
					
										match new_user_input4_6_2:
											
											case _: 
												if new_user_input4_6_2 != 0:  print("Invalid Input! Try Again..")
										
				
									#All Calls' Cost while loop ends
									


								case 3: 
									new_user_input4_6_3 = -1
									while new_user_input4_6_3 != 0:

										print(clear_counters())
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

							print(call_cost_settings())
							new_user_input4_7 = int(input("your choice: "))
					
							match new_user_input4_7:
								case 1: 
									new_user_input4_7_1 = -1
									while new_user_input4_7_1 != 0:

										print(call_cost_limit())
										new_user_input4_7_1 = int(input("your choice: "))
					
										match new_user_input4_7_1:
											case _: 
												if new_user_input4_7_1 != 0:  print("Invalid Input! Try Again..")
										
				
									#Call Cost Limit while loop ends
									


								case 2: 
									new_user_input4_7_2 = -1
									while new_user_input4_7_2 != 0:

										print(show_cost_in())
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

							print(prepaid_credit())
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

				print(tones())
				new_user_input5 = int(input("your choice: "))

				match new_user_input5:
					case 1: 	
		
						new_user_input5_1 = -1
						while new_user_input5_1 != 0:

							print(ringing_tone())
							new_user_input5_1 = int(input("your choice: "))
					
							match new_user_input5_1:
								
								case _: 
									if new_user_input5_1 != 0:  print("Invalid Input! Try Again..")
							
				
						#Ringing Tone while loop ends
						


					case 2: 	

						new_user_input5_2 = -1
						while new_user_input5_2 != 0:

							print(ringing_volume())
							new_user_input5_2 = int(input("your choice: "))
					
							match new_user_input5_2:
								
								case _: 
									if new_user_input5_2 != 0:  print("Invalid Input! Try Again..")
							
				
						#Ringing Volume Nos while loop ends
						

					
					case 3:		
					
						new_user_input5_3 = -1
						while new_user_input5_3 != 0:

							print(incoming_call_alert())
							new_user_input5_3 = int(input("your choice: "))
					
							match new_user_input5_3:
								
								case _: 
									if new_user_input5_3 != 0:  print("Invalid Input! Try Again..")
							
				
						#Incoming Call Alert  while loop ends
						


					case 4:	
						
						new_user_input5_4 = -1
						while new_user_input5_4 != 0:

							print(composer())
							new_user_input5_4 = int(input("your choice: "))
					
							match new_user_input5_4:
								
								case _: 
									if new_user_input5_4 != 0:  print("Invalid Input! Try Again..")
							
				
						#Composer while loop ends
						


					case 5: 	

						new_user_input5_5 = -1
						while new_user_input5_5 != 0:

							print(message_alert())
							new_user_input5_5 = int(input("your choice: "))
					
							match new_user_input5_5:
								
								case _: 
									if new_user_input5_5 != 0:  print("Invalid Input! Try Again..")
							
				
						#Message Alert Tone while loop ends
						
		

					case 6:		
					
						new_user_input5_6 = -1
						while new_user_input5_6 != 0:

							print(key_tones())
							new_user_input5_6 = int(input("your choice: "))
					
							match new_user_input5_6:
								
								case _: 
									if new_user_input5_6 != 0:  print("Invalid Input! Try Again..")
							
				
						#Key Tones while loop ends
						


					case 7: 	
		
						new_user_input5_7 = -1
						while new_user_input5_7 != 0:

							print(warning())
							new_user_input5_7 = int(input("your choice: "))
					
							match new_user_input5_7:
								
								case _: 
									if new_user_input5_7 != 0:  print("Invalid Input! Try Again..")
							
				
						#Warning and Game Tones while loop ends
						


					case 8: 	
		
						new_user_input5_8 = -1
						while new_user_input5_8 != 0:

							print(vibrating_alert())
							new_user_input5_8 = int(input("your choice: "))
					
							match new_user_input5_8:
								
								case _: 
									if new_user_input5_8 != 0:  print("Invalid Input! Try Again..")

							
				
						#Vibrating Alert while loop end
						


					case 9: 	
		
						new_user_input5_9 = -1
						while new_user_input5_9 != 0:

							print(screen_saver())
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

				print(settings())
				new_user_input6 = int(input("your choice: "))
					
				match new_user_input6:  
					case 1: 
		
						new_user_input6_1 = -1
						while new_user_input6_1 != 0:

							print(call_settings())
							new_user_input6_1 = int(input("your choice: "))
				
							match new_user_input6_1:  
								case 1: 
									new_user_input6_1_1 = -1
									while new_user_input6_1_1 != 0:

										print(automatic_redial())
										new_user_input6_1_1 = int(input("your choice: "))
					
										match new_user_input6_1_1:
											
											case _: 
												if new_user_input6_1_1 != 0:  print("Invalid Input! Try Again..")
										
				
									#Automatic Redial while loop ends
									


								case 2: 
									new_user_input6_1_2 = -1
									while new_user_input6_1_2 != 0:

										print(speed_dialing())
										new_user_input6_1_2 = int(input("your choice: "))
					
										match new_user_input6_1_2:
											
											case _: 
												if new_user_input6_1_2 != 0:  print("Invalid Input! Try Again..")
										
				
									#Speed Dialing while loop ends
									



								case 3: 
									new_user_input6_1_3 = -1
									while new_user_input6_1_3 != 0:

										print(call_waiting())
										new_user_input6_1_3 = int(input("your choice: "))
					
										match new_user_input6_1_3:
											
											case _: 
												if new_user_input6_1_3 != 0:  print("Invalid Input! Try Again..")
										
				
									#Call Waiting Options while loop ends
									



								case 4: 
									new_user_input6_1_4 = -1
									while new_user_input6_1_4 != 0:

										print(own_number())
										new_user_input6_1_4 = int(input("your choice: "))
					
										match new_user_input6_1_4:
											
											case _: 
												if new_user_input6_1_4 != 0:  print("Invalid Input! Try Again..")
										
				
									#Own Number Sending while loop ends
									



								case 5: 
									new_user_input6_1_5 = -1
									while new_user_input6_1_5 != 0:

										print(phone_line())
										new_user_input6_1_5 = int(input("your choice: "))
					
										match new_user_input6_1_5:
											
											case _: 
												if new_user_input6_1_5 != 0:  print("Invalid Input! Try Again..")
										
				
									#Phone Line in Use while loop ends
									


								case 6: 
									new_user_input6_1_6 = -1
									while new_user_input6_1_6 != 0:

										print(automatic_answer())
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

							print(phone_settings())
							new_user_input6_2 = int(input("your choice: "))
				
							match new_user_input6_2:


								case 1: 
									new_user_input6_2_1 = -1
									while new_user_input6_2_1 != 0:

										print(language())
										new_user_input6_2_1 = int(input("your choice: "))
					
										match new_user_input6_2_1:
											
											case _: 
												if new_user_input6_2_1 != 0:  print("Invalid Input! Try Again..")
										
				
									#Language while loop ends
									


								case 2: 
									new_user_input6_2_2 = -1
									while new_user_input6_2_2 != 0:

										print(call_info_display())
										new_user_input6_2_2 = int(input("your choice: "))
					
										match new_user_input6_2_2:
											
											case _: 
												if new_user_input6_2_2 != 0:  print("Invalid Input! Try Again..")
										
				
									#Call Info Display while loop ends
									



								case 3: 
									new_user_input6_2_3 = -1
									while new_user_input6_2_3 != 0:

										print(welcome_notes())
										new_user_input6_2_3 = int(input("your choice: "))
					
										match new_user_input6_2_3:
											
											case _: 
												if new_user_input6_2_3 != 0:  print("Invalid Input! Try Again..")
										
				
									#welcome Notes  while loop ends
									



								case 4: 
									new_user_input6_2_4 = -1
									while new_user_input6_2_4 != 0:

										print(network_selection())
										new_user_input6_2_4 = int(input("your choice: "))
					
										match new_user_input6_2_4:
											
											case _: 
												if new_user_input6_2_4 != 0:  print("Invalid Input! Try Again..")
										
				
									#Network Selection while loop ends
									


								case 5: 
									new_user_input6_2_5 = -1
									while new_user_input6_2_5 != 0:

										print(lights())
										new_user_input6_2_5 = int(input("your choice: "))
					
										match new_user_input6_2_5:
											
											case _: 
												if new_user_input6_2_5 != 0:  print("Invalid Input! Try Again..")
										
				
									#Lights while loop ends
									


								case 6: 
									new_user_input6_2_6 = -1
									while new_user_input6_2_6 != 0:

										print(sim_service_action())
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

							print(security_settings())
							new_user_input6_3 = int(input("your choice: "))
				
							match new_user_input6_3:


								case 1: 
									new_user_input6_3_1 = -1
									while new_user_input6_3_1 != 0:
		
										print(pin_code_request())
										new_user_input6_3_1 = int(input("your choice: "))
					
										match new_user_input6_3_1:
											
											case _: 
												if new_user_input6_3_1 != 0:  print("Invalid Input! Try Again..")
										
				
									#Pin Code Request while loop ends
									


								case 2: 
									new_user_input6_3_2 = -1
									while new_user_input6_3_2 != 0:

										print(call_barring_service())
										new_user_input6_3_2 = int(input("your choice: "))
					
										match new_user_input6_3_2:
											
											case _: 
												if new_user_input6_3_2 != 0:  print("Invalid Input! Try Again..")
										
				
									#Call Barring Service while loop ends
									


								case 3: 
									new_user_input6_3_3 = -1
									while new_user_input6_3_3 != 0:

										print(fixed_dialing())
										new_user_input6_3_3 = int(input("your choice: "))
					
										match new_user_input6_3_3:
											
											case _: 
												if new_user_input6_3_3 != 0:  print("Invalid Input! Try Again..")
										
				
									#Fixed Dialing Notes  while loop ends
									



								case 4: 
									new_user_input6_3_4 = -1
									while new_user_input6_3_4 != 0:

										print(closed_user_group())
										new_user_input6_3_4 = int(input("your choice: "))
					
										match new_user_input6_3_4:
											
											case _: 
												if new_user_input6_3_4 != 0:  print("Invalid Input! Try Again..")
										
				
									#Closed User Group while loop ends
									



								case 5: 
									new_user_input6_3_5 = -1
									while new_user_input6_3_5 != 0:

										print(phone_security())
										new_user_input6_3_5 = int(input("your choice: "))
					
										match new_user_input6_3_5:
											
											case _: 
												if new_user_input6_3_5 != 0:  print("Invalid Input! Try Again..")
										
				
									#Phone Security while loop ends
									


								case 6: 
									new_user_input6_3_6 = -1
									while new_user_input6_3_6 != 0:
	
										print(change_access_codes())
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

							print(restore_factory_settings())
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

				print(call_divert())
				new_user_input7 = int(input("your choice: "))
					
				match new_user_input7:
					
					case _: 
						if new_user_input7 != 0:  print("Invalid Input! Try Again..")
				
				
			#Call Divert while loop ends

		
		case 8:

			new_user_input8 = -1
			while new_user_input8 != 0:

				print(games())
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

				print(calculator())
				new_user_input9 = int(input("your choice: "))
					
				match new_user_input9:
					
					case _: 
						if new_user_input9 != 0:  print("Invalid Input! Try Again..")
				
				
			#Calculator while loop ends
			

		
		case 10: 	
			
			new_user_input10 = -1
			while new_user_input10 != 0:

				print(reminders())
				new_user_input10 = int(input("your choice: "))
					
				match new_user_input10:
					
					case _: 
						if new_user_input10 != 0:  print("Invalid Input! Try Again..")
				
				
			#Reminders while loop ends
			


		case 11:		

			new_user_input11 = 1
			while new_user_input11 != 0:

				print(clock())
				new_user_input11 = int(input("your choice: "))

				match new_user_input11:
		
					case 1: 	
		
						new_user_input11_1 = -1
						while new_user_input11_1 != 0:

							print(alarm_clock())
							new_user_input11_1 = int(input("your choice: "))
					
							match new_user_input11_1:
								
								case _: 
									if new_user_input11_1 != 0:  print("Invalid Input! Try Again..")
							


					case 2: 	

						new_user_input11_2 = -1
						while new_user_input11_2 != 0:

							print(clock_settings())
							new_user_input11_2 = int(input("your choice: "))
					
							match new_user_input11_2:
								
								case _: 
									if new_user_input11_2 != 0:  print("Invalid Input! Try Again..")
							
				
					
					case 3:		
					
						new_user_input11_3 = -1
						while new_user_input11_3 != 0:

							print(date_settings())
							new_user_input11_3 = int(input("your choice: "))
					
							match new_user_input11_3:
								
								case _: 
									if new_user_input11_3 != 0:  print("Invalid Input! Try Again..")
							


					case 4:	
						
						new_user_input11_4 = -1
						while new_user_input11_4 != 0:

							print(stopwatch())
							new_user_input11_4 = int(input("your choice: "))
					
							match new_user_input11_4:
								
								case _: 
									if new_user_input11_4 != 0:  print("Invalid Input! Try Again..")
							


					case 5: 	

						new_user_input11_5 = -1
						while new_user_input11_5 != 0:

							print(countdown_timer())
							new_user_input11_5 = int(input("your choice: "))
					
							match new_user_input11_5:
								
								case _: 
									if new_user_input11_5 != 0:  print("Invalid Input! Try Again..")

		

					case 6:		
					
						new_user_input11_6 = -1
						while new_user_input11_6 != 0:

							print(auto_update())
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

				print(profiles())
				new_user_input12 = int(input("your choice: "))
					
				match new_user_input12:
					
					case _: 
						if new_user_input12 != 0:  print("Invalid Input! Try Again..")
				
				
			#Profiles while loop ends

		
		case 13: 	
			
			new_user_input13 = -1
			while new_user_input13 != 0:

				print(sim_services())
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