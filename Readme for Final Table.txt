#features - 1324
#entries - 73815


ABOUT FEATURES
---------------
-cells having value -1 tells there is no data available corresponding that entry.

-columns corresponding to sessions table(in final_table.csv) contains frequency of that particular value for a particular user.

-"span"(in final_table.csv) tells about difference between date_account_created(from train_users_2.csv) and date_first_booking(from train_users_2.csv).

-"timestamp_first_active"(in train_users_2.csv) is divided into "date_in_month"(in final_table.csv contains value ranging(1-31)), "part_of_month"(["Start of month", "Mid month","End of month"]), "month"(in final_table.csv).

-"active_hours" contains no. of hours user was active for the first time.

-age(in train_users_2.csv) is divided in to bins called "age_bucket",['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54','55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '95-99', '100+']. Later on its  one-hot encoded.

-lat_destination, lng_destination, distance_km, destination_km2, destination_language, language_levenshtein_distance(in countries.csv) is one-hot encoded.

-secs_elapsed(in sessions.csv)is divided in to bins called "secs_elapsed_categories"(in final_table.csv [0,10800,21600,43200,86400,172800,1799949]).Later on its  one-hot encoded.

-action,action_type,device_type,action_detail(in sessions.csv) is one-hot encoded.

-on the basis of age_bucket, gender, country_destination(in age_gender_bkts.csv) a new feature is created "age_gender_dest"(in final_table.csv). Later on its  one-hot encoded.

-gender, signup_method, affiliate_channel, affiliate_provider, first_affiliate_tracked, signup_app, first_device_type, first_browser, country_destination(in train_users_2.csv) is one-hot encoded.


