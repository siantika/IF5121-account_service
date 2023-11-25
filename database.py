from abc import abstractmethod, ABC


class Database(ABC):
    """ Interface for database in account service """

    @abstractmethod
    def get_user_credentials(self):
        pass

    @abstractmethod
    def get_admin_credentials(self):
        pass


class DictDatabase(Database):
    """ Implementation using simpledict data type objects in python 3"""
    user_credentials = {
        'sian@gmail.com' : {
            'password' : 'akuganteng',
            'role' : 'user',
            'membership_status' : True,
            'number' : '001',
            'expiry_date' : None,
            'payment_status' : False
        },
        'nisa@gmail.com' : {
            'password' : 'qwery123',
            'role' : 'user',
            'membership_status' : None,
            'number' : '002',
            'expiry_date' : None,
            'payment_status' : 'belum'
        },
        'dicky@yahoo.com' : {
            'password' : 'husqivarna',
            'role' : 'user',
            'membership_status' : None ,
            'number' : '003',
            'expiry_date' : None,
            'payment_status' : False
        }
    }

    admin_credentials = {
        'evita@studio21.com' : {
            'password' : 'lexus231',
            'role' : 'admin',
            'admin_number' : '001',
        },
    }

    def get_user_credentials(self):
        return self.user_credentials
    
    def get_admin_credentials(self):
        return self.admin_credentials