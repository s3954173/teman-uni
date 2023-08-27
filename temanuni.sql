CREATE TABLE `user`(
    `user_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL
);
CREATE TABLE `messages`(
    `message_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `sender_id` BIGINT UNSIGNED NOT NULL,
    `receiver_id` BIGINT UNSIGNED NOT NULL,
    `message_text` TEXT NOT NULL,
    `timestamp` DATETIME NOT NULL
);
CREATE TABLE `profile_interests`(
    `profile_id` BIGINT UNSIGNED NOT NULL,
    `interest_id` INT UNSIGNED NULL
);
ALTER TABLE
    `profile_interests` ADD PRIMARY KEY(`profile_id`, `interest_id`);
CREATE TABLE `profile`(
    `profile_id` BIGINT UNSIGNED NOT NULL,
    `dob` DATE NOT NULL,
    `gender` VARCHAR(255) NOT NULL,
    `first_name` VARCHAR(255) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL,
    `location` VARCHAR(255) NOT NULL,
    `university` VARCHAR(255) NOT NULL,
    `course` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `profile` ADD PRIMARY KEY(`profile_id`);
CREATE TABLE `event_users_going`(
    `event_id` BIGINT UNSIGNED NOT NULL,
    `user_id` BIGINT UNSIGNED NOT NULL
);
ALTER TABLE
    `event_users_going` ADD PRIMARY KEY(`event_id`, `user_id`);
CREATE TABLE `event_invited_users`(
    `event_id` BIGINT UNSIGNED NOT NULL,
    `user_id` BIGINT UNSIGNED NOT NULL
);
ALTER TABLE
    `event_invited_users` ADD PRIMARY KEY(`event_id`, `user_id`);
CREATE TABLE `photos`(
    `photo_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `profile_id` BIGINT UNSIGNED NOT NULL,
    `photo_filename` VARCHAR(255) NOT NULL,
    `photo_path` VARCHAR(255) NOT NULL
);
CREATE TABLE `interests`(
    `interest_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `interest` VARCHAR(255) NOT NULL
);
CREATE TABLE `languages`(
    `language_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `language` VARCHAR(255) NOT NULL
);
CREATE TABLE `event_users_declined`(
    `event_id` BIGINT UNSIGNED NOT NULL,
    `user_id` BIGINT UNSIGNED NOT NULL
);
ALTER TABLE
    `event_users_declined` ADD PRIMARY KEY(`event_id`, `user_id`);
CREATE TABLE `events`(
    `event_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `event_name` VARCHAR(255) NOT NULL,
    `start_date` DATE NOT NULL,
    `start_time` TIME NOT NULL,
    `description` TEXT NOT NULL,
    `creator_id` BIGINT UNSIGNED NOT NULL
);
CREATE TABLE `profile_languages`(
    `profile_id` BIGINT UNSIGNED NOT NULL,
    `language_id` INT UNSIGNED NOT NULL
);
ALTER TABLE
    `profile_languages` ADD PRIMARY KEY(`profile_id`, `language_id`);
ALTER TABLE
    `event_users_declined` ADD CONSTRAINT `event_users_declined_event_id_foreign` FOREIGN KEY(`event_id`) REFERENCES `events`(`event_id`);
ALTER TABLE
    `event_users_going` ADD CONSTRAINT `event_users_going_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `photos` ADD CONSTRAINT `photos_profile_id_foreign` FOREIGN KEY(`profile_id`) REFERENCES `profile`(`profile_id`);
ALTER TABLE
    `messages` ADD CONSTRAINT `messages_receiver_id_foreign` FOREIGN KEY(`receiver_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `event_users_declined` ADD CONSTRAINT `event_users_declined_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `messages` ADD CONSTRAINT `messages_sender_id_foreign` FOREIGN KEY(`sender_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `profile` ADD CONSTRAINT `profile_profile_id_foreign` FOREIGN KEY(`profile_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `profile_interests` ADD CONSTRAINT `profile_interests_profile_id_foreign` FOREIGN KEY(`profile_id`) REFERENCES `profile`(`profile_id`);
ALTER TABLE
    `profile_languages` ADD CONSTRAINT `profile_languages_profile_id_foreign` FOREIGN KEY(`profile_id`) REFERENCES `profile`(`profile_id`);
ALTER TABLE
    `profile_languages` ADD CONSTRAINT `profile_languages_language_id_foreign` FOREIGN KEY(`language_id`) REFERENCES `languages`(`language_id`);
ALTER TABLE
    `profile_interests` ADD CONSTRAINT `profile_interests_interest_id_foreign` FOREIGN KEY(`interest_id`) REFERENCES `interests`(`interest_id`);
ALTER TABLE
    `event_users_going` ADD CONSTRAINT `event_users_going_event_id_foreign` FOREIGN KEY(`event_id`) REFERENCES `events`(`event_id`);
ALTER TABLE
    `event_invited_users` ADD CONSTRAINT `event_invited_users_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `event_invited_users` ADD CONSTRAINT `event_invited_users_event_id_foreign` FOREIGN KEY(`event_id`) REFERENCES `events`(`event_id`);
ALTER TABLE
    `events` ADD CONSTRAINT `events_creator_id_foreign` FOREIGN KEY(`creator_id`) REFERENCES `user`(`user_id`);
-- Insert data into the 'user' table
INSERT INTO `user` (`email`, `password`)
VALUES ('user1@example.com', 'password1'),
       ('user2@example.com', 'password2'),
       ('user3@example.com', 'password3');

-- Insert data into the 'profile' table
INSERT INTO `profile` (`profile_id`, `dob`, `gender`, `first_name`, `last_name`, `location`, `university`, `course`)
VALUES (1, '1990-01-01', 'Male', 'John', 'Doe', 'City A', 'University A', 'Course A'),
       (2, '1995-05-15', 'Female', 'Jane', 'Smith', 'City B', 'University B', 'Course B'),
       (3, '1988-11-30', 'Male', 'Michael', 'Johnson', 'City C', 'University C', 'Course C');

-- Insert data into the 'interests' table
INSERT INTO `interests` (`interest`)
VALUES ('Sports'), ('Music'), ('Travel');

-- Insert data into the 'profile_interests' table
INSERT INTO `profile_interests` (`profile_id`, `interest_id`)
VALUES (1, 1),
       (1, 2),
       (2, 2),
       (3, 3);

-- Insert data into the 'languages' table
INSERT INTO `languages` (`language`)
VALUES ('English'), ('Spanish'), ('French');

-- Insert data into the 'profile_languages' table
INSERT INTO `profile_languages` (`profile_id`, `language_id`)
VALUES (1, 1),
       (1, 2),
       (2, 1),
       (3, 3);

-- Insert data into the 'events' table
INSERT INTO `events` (`event_name`, `start_date`, `start_time`, `description`, `creator_id`)
VALUES ('Event 1', '2023-08-20', '12:00:00', 'Description for Event 1', 1),
       ('Event 2', '2023-08-25', '15:30:00', 'Description for Event 2', 2);

-- Insert data into the 'event_users_going' table
INSERT INTO `event_users_going` (`event_id`, `user_id`)
VALUES (1, 1),
       (1, 2),
       (2, 2),
       (2, 3);

-- Insert data into the 'event_invited_users' table
INSERT INTO `event_invited_users` (`event_id`, `user_id`)
VALUES (1, 1),
       (1, 3),
       (2, 1),
       (2, 3);

-- Insert data into the 'messages' table
INSERT INTO `messages` (`sender_id`, `receiver_id`, `message_text`, `timestamp`)
VALUES (1, 2, 'Hello from User 1 to User 2', NOW()),
       (2, 1, 'Hello from User 2 to User 1', NOW());
