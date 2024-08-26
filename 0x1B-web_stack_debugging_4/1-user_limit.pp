# increase the Limit for Holberton open files

# increase hard file limits
exec { 'increase-hard-file-limit-holberton-user':
  command => 'sed -i "/^holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# increase Soft File limit
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
