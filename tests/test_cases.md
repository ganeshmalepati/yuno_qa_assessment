PURCHASE FLOW
Test Case	        Description	                        Type	            Suite
TC_P_01	            Purchase with minimal fields	    Functional	        Sanity
TC_P_02	            Purchase with max fields	        Functional	        Regression
TC_P_03	            Missing workflow	                Negative	        Sanity
TC_P_04	            Invalid card number	                Negative	        Regression



AUTHORIZATION + CAPTURE + REFUND FLOW
Test Case	        Description	                        Type	            Suite
TC_A_01	            Authorization only	                Functional	        Sanity
TC_A_02	            Capture authorized payment	        Functional	        Integration
TC_A_03	            Refund captured payment	            Functional	        Integration
TC_A_04	            Capture without authorization	    Negative	        Regression


VERIFY FLOW
Test Case	        Description	                        Type	            Suite
TC_V_01	            Card verification	                Functional	        Sanity
TC_V_02	            Verify with invalid card	        Negative	        Sanity



NON-FUNCTIONAL REQUIREMENTS

-> API response < 2 seconds
-> Idempotency enforced
-> Secure credential handling
-> API error consistency

			

