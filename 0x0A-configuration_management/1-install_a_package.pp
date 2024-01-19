# 1-install_a_package.pp

# Define package resource for Flask
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Notify for verification
notify { 'Flask installed':
  message => 'Flask 2.1.0 has been installed successfully.',
}
