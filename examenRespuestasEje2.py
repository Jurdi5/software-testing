import unittest
from unittest.mock import patch, MagicMock
import sys
from io import StringIO

try:
    from examenEje2 import Song, SongStore
except ImportError:
    print("Error: No se pudo importar el módulo. Asegúrate de que el archivo 'examenEje2.py' esté en el mismo directorio")
    sys.exit(1)

class TestSong(unittest.TestCase):
    def test_song_creation(self):
        song = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", 1975)
        self.assertEqual(song.title, "Bohemian Rhapsody")
        self.assertEqual(song.author, "Queen")
        self.assertEqual(song.album, "A Night at the Opera")
        self.assertEqual(song.year, 1975)
    
    def test_song_attributes_types(self):
        song = Song("Test Song", "Test Author", "Test Album", 2020)
        self.assertIsInstance(song.title, str)
        self.assertIsInstance(song.author, str)
        self.assertIsInstance(song.album, str)
        self.assertIsInstance(song.year, int)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_song_display(self, mock_stdout):
        """Verifica que el método display imprima correctamente"""
        song = Song("Test Song", "Test Author", "Test Album", 2020)
        song.display()
        output = mock_stdout.getvalue()
        self.assertIn("Title: Test Song", output)
        self.assertIn("Author: Test Author", output)
        self.assertIn("Album: Test Album", output)
        self.assertIn("Year: 2020", output)

class TestSongStore(unittest.TestCase):
    def setUp(self):
        self.store = SongStore()
        self.song1 = Song("Song 1", "Author 1", "Album 1", 2020)
        self.song2 = Song("Song 2", "Author 2", "Album 2", 2021)
        self.song3 = Song("Song 3", "Author 3", "Album 3", 2022)
    
    def test_songstore_initialization(self):
        store = SongStore()
        self.assertEqual(store.songs, [])
        self.assertIsInstance(store.songs, list)
    
    @patch('builtins.print')
    def test_add_song(self, mock_print):
        self.store.add_song(self.song1)
        self.assertEqual(len(self.store.songs), 1)
        self.assertEqual(self.store.songs[0], self.song1)
        mock_print.assert_called_with("Song 'Song 1' added to the store.")
    
    @patch('builtins.print')
    def test_add_multiple_songs(self, mock_print):
        self.store.add_song(self.song1)
        self.store.add_song(self.song2)
        self.store.add_song(self.song3)
        self.assertEqual(len(self.store.songs), 3)
        self.assertIn(self.song1, self.store.songs)
        self.assertIn(self.song2, self.store.songs)
        self.assertIn(self.song3, self.store.songs)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_songs_with_songs(self, mock_stdout):
        self.store.add_song(self.song1)
        self.store.add_song(self.song2)
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.store.display_songs()
        output = mock_stdout.getvalue()
        self.assertIn("Songs available in the store:", output)
        self.assertIn("Song 1", output)
        self.assertIn("Song 2", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_songs_single(self, mock_stdout):
        self.store.add_song(self.song1)
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.store.display_songs()
        output = mock_stdout.getvalue()
        self.assertIn("Song 1", output)
        self.assertIn("Author 1", output)
        self.assertIn("Album 1", output)
        self.assertIn("2020", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_search_song_found(self, mock_stdout):
        self.store.add_song(self.song1)
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.store.search_song("Song 1")
        output = mock_stdout.getvalue()
        self.assertIn("Found 1 song(s) with title 'Song 1':", output)
        self.assertIn("Song 1", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_search_song_not_found(self, mock_stdout):
        self.store.add_song(self.song1)
        self.store.search_song("Nonexistent Song")
        output = mock_stdout.getvalue()
        self.assertIn("No song found with title 'Nonexistent Song'.", output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_search_empty_store(self, mock_stdout):
        self.store.search_song("Any Song")
        output = mock_stdout.getvalue()
        self.assertIn("No song found with title 'Any Song'.", output)
    
class TestSongIntegration(unittest.TestCase):
    def setUp(self):
        """Configura el entorno de prueba"""
        self.store = SongStore()
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_complete_workflow(self, mock_stdout):
        song1 = Song("Imagine", "John Lennon", "Imagine", 1971)
        song2 = Song("Yesterday", "The Beatles", "Help!", 1965)
        
        self.store.add_song(song1)
        self.store.add_song(song2)
        
        self.assertEqual(len(self.store.songs), 2)
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.store.display_songs()
        output = mock_stdout.getvalue()
        self.assertIn("Imagine", output)
        self.assertIn("Yesterday", output)
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.store.search_song("Imagine")
        output = mock_stdout.getvalue()
        self.assertIn("Found 1 song(s)", output)
        self.assertIn("John Lennon", output)

if __name__ == "__main__":
    unittest.main(verbosity=2)