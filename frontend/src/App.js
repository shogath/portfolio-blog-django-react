import {
    BrowserRouter as Router,
    Route,
    Routes
} from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";

import Header from './components/Header'
import Footer from "./components/Footer";
import PostListPage from './pages/PostListPage'
import PostPage from './pages/PostPage'
import PopularPosts from "./components/PopularPosts";
import LoginPage from './pages/LoginPage'
import RegisterPage from "./pages/RegisterPage";
import PageNotFound from "./pages/PageNotFound";

function App() {
    return (
        <Router>
            <div className="w3-content" style={{ width: 100 + '%', maxWidth: 1400 + 'px' }}>
                <div className="w3-row">
                    <AuthProvider>
                        <Header />
                        <Routes>
                            <Route path="blog/" exact element={<PostListPage />} />
                            <Route path="blog/:slug" element={<PostPage />} />
                            <Route path="blog/login" element={<LoginPage />} />
                            <Route path="blog/register" element={<RegisterPage />} />
                            <Route path="*" element={<PageNotFound />} />
                        </Routes>
                        <PopularPosts />
                    </AuthProvider>
                </div>
            </div>
            <div style={{ flexGrow: 1 }}></div>
            <Footer />
        </Router>
    );
}

export default App;
