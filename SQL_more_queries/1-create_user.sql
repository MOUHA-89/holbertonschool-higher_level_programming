-- Créer l'utilisateur user_0d_1 s'il n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorder tous les privilèges à user_0d_1 sur l'ensemble du serveur MySQL
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%' WITH GRANT OPTION;

-- Appliquer les modifications de privilèges immédiatement
FLUSH PRIVILEGES;
