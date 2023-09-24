CREATE TABLE `user`(
    `user_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `last_login` DATETIME NULL
);
CREATE TABLE `messages`(
    `message_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `sender_id` BIGINT UNSIGNED NOT NULL,
    `receiver_id` BIGINT UNSIGNED NOT NULL,
    `message_text` TEXT NOT NULL,
    `timestamp` DATETIME NOT NULL
);
CREATE TABLE `friends`(
    `user1_id` BIGINT UNSIGNED NOT NULL,
    `user2_id` BIGINT UNSIGNED NOT NULL,
    `user1_interest` TINYINT(1) NOT NULL,
    `user2_interest` TINYINT(1) NOT NULL,
    `friends_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
);
CREATE TABLE `profile_interests`(
    `profile_id` BIGINT UNSIGNED NOT NULL,
    `interest_id` INT UNSIGNED NULL,
    `profileinterests_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
);
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
    `user_id` BIGINT UNSIGNED NOT NULL,
    `going_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
);
CREATE TABLE `event_invited_users`(
    `event_id` BIGINT UNSIGNED NOT NULL,
    `user_id` BIGINT UNSIGNED NOT NULL,
    `invited_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
);
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
    `user_id` BIGINT UNSIGNED NOT NULL,
    `declined_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
);
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
    `language_id` INT UNSIGNED NOT NULL,
    `profilelanguage_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
);
ALTER TABLE
    `event_users_declined` ADD CONSTRAINT `event_users_declined_event_id_foreign` FOREIGN KEY(`event_id`) REFERENCES `events`(`event_id`);
ALTER TABLE
    `event_users_going` ADD CONSTRAINT `event_users_going_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `photos` ADD CONSTRAINT `photos_profile_id_foreign` FOREIGN KEY(`profile_id`) REFERENCES `profile`(`profile_id`);
ALTER TABLE
    `friends` ADD CONSTRAINT `friends_user1_id_foreign` FOREIGN KEY(`user1_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `messages` ADD CONSTRAINT `messages_receiver_id_foreign` FOREIGN KEY(`receiver_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `event_users_declined` ADD CONSTRAINT `event_users_declined_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `messages` ADD CONSTRAINT `messages_sender_id_foreign` FOREIGN KEY(`sender_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `profile` ADD CONSTRAINT `profile_profile_id_foreign` FOREIGN KEY(`profile_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `friends` ADD CONSTRAINT `friends_user2_id_foreign` FOREIGN KEY(`user2_id`) REFERENCES `user`(`user_id`);
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