json.array!(@employments) do |employment|
  json.extract! employment, :id, :title, :description
  json.url employment_url(employment, format: :json)
end
