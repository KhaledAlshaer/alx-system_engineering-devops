# install puppet-lint gem.

package { 'puppet-lint':
  ensure          => '2.5.0',
  provider        => 'gem',
  install_options => ['--no-document'],
}
