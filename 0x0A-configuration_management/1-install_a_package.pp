# 1-install_a_package.p

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

