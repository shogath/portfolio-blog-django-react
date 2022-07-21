import React, { useState, useEffect } from 'react'
import PostItem from '../components/PostItem'
import axiosInstance from '../utils/axiosInstanse'
import Pagination from '../components/Pagination'

const PostListPage = () => {

    const [posts, setPosts] = useState([])
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPageCount, setTotalPageCount] = useState(null);
    const [totalCount, setTotalCount] = useState(null);
    const [nextPage, setNextPage] = useState(false);
    const [previousPage, setPreviousPage] = useState(false);

    useEffect(() => {
        // Prevent multiple api calls
        const controller = new AbortController();
        const getPosts = async () => {
            try {
                let response = await axiosInstance.get(`/blog/api/index/?page=${currentPage}`, {
                    signal: controller.signal,
                })
                document.title = 'Posts'
                setTotalPageCount(response.data.total_pages)
                setTotalCount(response.data.count)
                setNextPage(response.data.next)
                setPreviousPage(response.data.previous)
                setPosts(response.data.results)
            } catch (err) {
                // console.log('There was a problem or request was cancelled.')
            }
        }
        getPosts()
        window.scrollTo(0, 0)
        return () => controller.abort()
    }, [currentPage])

    return (
        <div className="w3-col l8 s12">
            {posts?.map((post, index) => (
                <PostItem key={index} post={post} />
            ))}
            <Pagination
                totalPageCount={totalPageCount}
                currentPage={currentPage}
                nextPage={nextPage}
                previousPage={previousPage}
                onPageChange={page => setCurrentPage(page)}
            />
        </div>
    );
}

export default PostListPage;
