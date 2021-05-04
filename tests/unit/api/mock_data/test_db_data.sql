INSERT INTO roles (id, name, description) VALUES ('3b12c6ef-bb75-498c-9269-e8989762c59c', 'name_1', 'description_1');
INSERT INTO roles (id, name, description) VALUES ('4e2bed46-6fc3-4a82-8c6d-ea9718367aaa', 'name_2', 'description_2');
INSERT INTO roles (id, name, description) VALUES ('be807485-11bd-45a4-b3f1-ccb97d8d7c33', 'name_3', 'description_3');

INSERT INTO users (id, email, psw) VALUES ('bbc3e3b3-fe98-4fab-a5ae-b153c9c8cc9c', 'test1@mail', 'adsxaewdaqwd');
INSERT INTO users (id, email, psw) VALUES ('c5016ef9-9b8c-4ada-b401-cc6166336224', 'test2@mail', 'adwdaswdzsd');
INSERT INTO users (id, email, psw) VALUES ('aeb1c933-d5e5-4395-8e00-26404e9d6412', 'test3@mail', 'afevsevf');
INSERT INTO users (id, email, psw) VALUES ('e8d13e68-e49e-4707-9d8f-ffcdd7ce1270', 'test4@mail', 'aesrtbdrby');
INSERT INTO users (id, email, psw) VALUES ('b26e12f7-3235-4882-ae6a-11367ab1a862', 'test5@mail', 'festbrdtby');

INSERT INTO user_role (user_id, role_id) VALUES ('bbc3e3b3-fe98-4fab-a5ae-b153c9c8cc9c', '3b12c6ef-bb75-498c-9269-e8989762c59c');
INSERT INTO user_role (user_id, role_id) VALUES ('e8d13e68-e49e-4707-9d8f-ffcdd7ce1270', '4e2bed46-6fc3-4a82-8c6d-ea9718367aaa');
INSERT INTO user_role (user_id, role_id) VALUES ('b26e12f7-3235-4882-ae6a-11367ab1a862', '4e2bed46-6fc3-4a82-8c6d-ea9718367aaa');
INSERT INTO user_role (user_id, role_id) VALUES ('b26e12f7-3235-4882-ae6a-11367ab1a862', 'be807485-11bd-45a4-b3f1-ccb97d8d7c33');
INSERT INTO user_role (user_id, role_id) VALUES ('e8d13e68-e49e-4707-9d8f-ffcdd7ce1270', 'be807485-11bd-45a4-b3f1-ccb97d8d7c33');
INSERT INTO user_role (user_id, role_id) VALUES ('aeb1c933-d5e5-4395-8e00-26404e9d6412', 'be807485-11bd-45a4-b3f1-ccb97d8d7c33');
INSERT INTO user_role (user_id, role_id) VALUES ('c5016ef9-9b8c-4ada-b401-cc6166336224', 'be807485-11bd-45a4-b3f1-ccb97d8d7c33');