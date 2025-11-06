"""
Configuration Service - Business logic for configuration data
"""
from app.daos.interfaces import ConfigurationDAO
from app.daos.json.configuration_dao_json import ConfigurationDAOJSON


class ConfigurationService:
    """Service for configuration business logic"""
    
    def __init__(self, dao: ConfigurationDAO = None):
        self.dao = dao if dao is not None else ConfigurationDAOJSON()
    
    def get_all_configuration(self):
        """Get all configuration"""
        return self.dao.get_all()
    
    def get_configuration(self):
        """Get configuration (returns first or random)"""
        data = self.dao.get_all()
        configs = data.get('configuration', [])
        if configs:
            return configs[0]  # Return first config, can be modified to return random
        return {'config': 'No configuration available'}

