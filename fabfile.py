import os
from fabric.colors import white, green, red, blue, yellow
from fabric.api import cd, env, prefix, run, sudo, local
env.local_root = os.path.dirname(os.path.abspath(__file__))

def jasmine():
    """
    RUN the jasmine test suite
    """
    with cd(env.local_root):
        test_result = local('jasmine-headless-webkit')
        return test_result.succeeded
    
def install_jasmine():
    """
    install jasmine environment
    """
    local("brew install qt")
    local("bash -s stable < <(curl -s https://raw.github.com/wayneeseguin/rvm/master/binscripts/rvm-installer)")
    print red(""" paste this in your .profile [[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm" # This loads RVM into a shell session.""")
    print yellow('once inserted, type the name of your rc file [.profile/.bashrc/.bash_profile]:')
    profile_location = raw_input().strip()
    local("source ~/%s" % profile_location)
    local("rvm install 1.9.2")
    local("rvm use 1.9.2@milely --create --default")
    local("gem install jasmine")
    #    local("gem install jasmine-headless-webkit")
    # https://github.com/johnbintz/jasmine-headless-webkit.git
    # check project out
    # gem build .gemfile
    # gem install jasmine-*.gem

