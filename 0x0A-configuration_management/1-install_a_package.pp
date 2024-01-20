# 1-install_a_package.pp

# Define package resource for Flask
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Specify version for Werkzeug
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['Flask'],
}
