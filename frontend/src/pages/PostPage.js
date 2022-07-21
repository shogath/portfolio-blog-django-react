import React, { useState, useEffect, useContext } from 'react'
import { useParams, Link } from 'react-router-dom';
import axiosInstance from '../utils/axiosInstanse'
import AuthContext from '../context/AuthContext';
import PageNotFound from './PageNotFound';
import Pagination from '../components/Pagination';

const PostPage = () => {

    let { user } = useContext(AuthContext)
    const { slug } = useParams()
    const [post, setPost] = useState(null)
    const [status, setStatus] = useState(null)

    const [currentPage, setCurrentPage] = useState(1);
    const [totalPageCount, setTotalPageCount] = useState(null);
    const [nextPage, setNextPage] = useState(null);
    const [previousPage, setPreviousPage] = useState(null);

    useEffect(() => {
        // Prevent multiple api calls
        const controller = new AbortController();
        const getPost = async () => {
            try {
                let response = await axiosInstance.get(`/blog/api/${slug}/?page=${currentPage}`, {
                    signal: controller.signal,
                })
                setPost(response.data)
                setTotalPageCount(response.data.pagination_data.total_pages)
                setNextPage(response.data.pagination_data.next)
                setPreviousPage(response.data.pagination_data.previous)
                document.title = response.data.title
                setStatus(200)
            } catch (err) {
                setStatus(404)
            }
        }
        getPost()
        return () => controller.abort()
    }, [slug, currentPage])

    const handleSubmit = (event) => {
        event.preventDefault();
        // Prevent multiple api calls
        const controller = new AbortController();
        const sendComment = async () => {
            try {
                await axiosInstance.post('/blog/api/add-comment/', {
                    signal: controller.signal,
                    post: post?.slug,
                    text: event.target.Comment.value
                })
            } catch (err) {
                // console.log('There was a problem or request was cancelled.')
            }
        }
        sendComment()
        window.location.reload(false);
        return () => controller.abort()
    }

    if (status === 404) {
        return (
            <PageNotFound />
        )
    } else {
        return (
            <div className="w3-col l8 s12">
                <div className="w3-card-4 w3-margin w3-white">
                    <img src={post?.image} alt={post?.title} className="post-img" />
                    <div className="w3-container">
                        <h3><b>{post?.title}</b></h3>
                        <h5><span className="w3-opacity">{post?.date}</span></h5>
                    </div>

                    <div className="w3-container">
                        <p dangerouslySetInnerHTML={{ __html: post?.content }}></p>
                    </div>
                    <hr />
                </div>
                <div id="comments" className="w3-card-4 w3-margin">
                    <div className="w3-container w3-padding">
                        <h4><b>Comments</b></h4>
                    </div>
                    <ul className="w3-ul w3-white">
                        {post?.comments?.length ? post?.comments.map((comment, index) => (
                            <li key={index} className="w3-padding-16">
                                <span className="w3-large"><b>{comment.username}</b></span><br />
                                <span>{comment.text}</span>
                            </li>
                        )) : <div className="w3-container w3-padding w3-margin">No comments here yet...</div>}
                    </ul>
                </div>
                <Pagination
                    totalPageCount={totalPageCount}
                    currentPage={currentPage}
                    nextPage={nextPage}
                    previousPage={previousPage}
                    onPageChange={page => setCurrentPage(page)}
                />
                <div className="w3-card-4 w3-margin w3-padding-large w3-grey">
                    <div className="w3-container w3-padding">
                        <h4><b>Add a comment</b></h4>
                    </div>

                    {/* 
                        Show comment form if user is authenticated 
                    */}

                    {user ? (
                        <form id="comment-form" onSubmit={handleSubmit}>
                            <div className="w3-section">
                                <textarea
                                    className="w3-input w3-border"
                                    type="text"
                                    name="Comment"
                                    form="comment-form"
                                    rows="7"
                                    cols="50"
                                    style={{ resize: 'none' }}
                                    required
                                />
                            </div>
                            <button type="submit" className="w3-button w3-black w3-margin-bottom">
                                <i className="fa fa-paper-plane"></i>Add a comment
                            </button>
                        </form>) : (
                        <div className="w3-container w3-padding w3-white">
                            <h6>
                                <Link to={'/blog/register'}>
                                    <span className="w3-button w3-black">Sign Up</span>
                                </Link>
                                &nbsp;&nbsp; or &nbsp;&nbsp;
                                <Link to={'/blog/login'}>
                                    <span className="w3-button w3-black">Login</span>
                                </Link>
                                &nbsp;&nbsp; to add a comment.
                            </h6>
                        </div>
                    )}
                </div>
            </div>
        );
    }
}

export default PostPage;
