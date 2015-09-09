import getpass

import pytest

import pamela


def test_pam_error_noargs():
    e = pamela.PAMError()
    s = str(e)
    r = repr(e)
    assert 'Unknown' in s
    assert 'Unknown' in r


def test_pam_error_errno():
    en = pamela.ERRNO.PAM_USER_UNKNOWN
    e = pamela.PAMError(errno=en)
    assert str(en) in str(e)
    assert 'user' in str(e)


def test_auth_nouser():
    with pytest.raises(pamela.PAMError) as exc_info:
        pamela.authenticate('userdoesntexist', 'wrongpassword')
    
    err = exc_info.value
    assert err.errno == pamela.ERRNO.PAM_USER_UNKNOWN
    assert 'user' in str(err)


def test_auth_badpassword():
    with pytest.raises(pamela.PAMError) as exc_info:
        pamela.authenticate(getpass.getuser(), 'wrongpassword')

    err = exc_info.value
    assert err.errno == pamela.ERRNO.PAM_AUTH_ERR
    assert 'authentication' in str(err)


def test_all():
    for name in pamela.__all__:
        getattr(pamela, name)
