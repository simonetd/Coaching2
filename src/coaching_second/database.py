import sqlite3

class DatabaseManager:
    def __init__(self, db_name="market_data.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def create_tables(self):
        """Création de la table des statistiques uniquement."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS statistics_data (
                instrument_id TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                bid_mean REAL,
                ask_mean REAL,
                bid_std REAL,
                ask_std REAL
            )
        ''')
        self.conn.commit()

    def insert_statistics(self, instrument_id, bid_mean, ask_mean, bid_std, ask_std):
        """Insertion des statistiques en base."""
        self.cursor.execute('''
            INSERT INTO statistics_data (instrument_id, bid_mean, ask_mean, bid_std, ask_std)
            VALUES (?, ?, ?, ?, ?)
        ''', (instrument_id, bid_mean, ask_mean, bid_std, ask_std))
        self.conn.commit()
