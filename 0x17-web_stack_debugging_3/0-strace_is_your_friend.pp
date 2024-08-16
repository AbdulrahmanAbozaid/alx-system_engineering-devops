# a puppet to fix a wordpress site issue while running on apache server
# editing the mistyped .phpp into php in /var/www/html/wp-settings.php file

exec { 'fix-wordpress-server-error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/bin/:/bin/',
}
