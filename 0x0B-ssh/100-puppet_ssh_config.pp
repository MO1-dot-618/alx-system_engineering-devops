#using puppet to automate configuration

file { '/etc/ssh/ssh_config':
	ensure => 'present',
	content => "
	Include /etc/ssh/ssh_config.d/*.conf
	Host *
	PasswordAuthentication no
	IdentityFile ~/.ssh/school",
}
